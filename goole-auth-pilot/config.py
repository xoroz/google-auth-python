from dotenv import load_dotenv
import os
import logging

# Load environment variables from .env file
load_dotenv()

try:
    # Setting up configuration variables
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
    FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
    CALLBACK_URL = os.getenv("CALLBACK_URL")
    #allow https to http for testing
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

    print(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, FLASK_SECRET_KEY, CALLBACK_URL)
    if not all([GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, FLASK_SECRET_KEY, CALLBACK_URL]):
        logging.error("One or more environment variables are missing. Please check your .env file.")

    logging.info("Environment variables loaded successfully.")
except Exception as e:
    logging.error("Error loading environment variables: %s", str(e), exc_info=True)