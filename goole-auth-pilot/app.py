from flask import Flask, render_template
import logging
from config import FLASK_SECRET_KEY  # Import FLASK_SECRET_KEY
from blueprints.auth import auth_blueprint, google_blueprint
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.secret_key = FLASK_SECRET_KEY  # Configure the Flask app's secret key
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(google_blueprint, url_prefix="/login")

@app.route('/')
def home():
    logging.info('Rendering homepage with Login with Google button')
    try:
        return render_template('index.html')
    except Exception as e:
        logging.error("Error rendering homepage: %s", e, exc_info=True)
        return "An error occurred while rendering the homepage", 500

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        app.run(host='0.0.0.0', port=8000)
    except Exception as e:
        logging.error("Error starting the Flask application: %s", e, exc_info=True)