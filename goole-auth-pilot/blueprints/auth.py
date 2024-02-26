from flask import Blueprint, redirect, url_for, flash, render_template
from flask_dance.contrib.google import make_google_blueprint, google
import os
import logging

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')

google_blueprint = make_google_blueprint(
    client_id=os.environ.get("GOOGLE_CLIENT_ID"),
    client_secret=os.environ.get("GOOGLE_CLIENT_SECRET"),
    offline=True,
    scope=["profile", "email"],
    redirect_to="auth.callback"
)

@auth_blueprint.route('/login')
def login():
    try:
        if not google.authorized:
            logging.info("Redirecting user to Google login")
            return redirect(url_for("google.login"))
        logging.info("User already authenticated, redirecting to callback")
        return redirect(url_for('.callback'))
    except Exception as e:
        logging.error("Error during login redirection: %s", e, exc_info=True)
        return "An error occurred during login redirection", 500

@auth_blueprint.route('/callback')
def callback():
    try:
        if not google.authorized:
            flash("You denied the request to sign in.")
            logging.info("User denied the request to sign in.")
            return redirect(url_for("auth.login"))

        resp = google.get("/oauth2/v2/userinfo")
        assert resp.ok, resp.text
        email = resp.json()["email"]
        token = google.token["access_token"]  # Retrieve the access token
        logging.info("Successfully retrieved user information: email={}, token={}".format(email, token))

        return render_template("profile.html", email=email, token=token)
    except Exception as e:
        logging.error("Error handling OAuth callback: %s", e, exc_info=True)
        return "An error occurred during OAuth callback handling", 500