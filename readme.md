# Goole-Auth-Pilot

Goole-Auth-Pilot is a web-based Python Flask application designed to demonstrate the integration of Google API for user authentication. The application showcases the OAuth 2.0 authentication flow, enabling users to log in using their Google account, and displays the user's email and token upon successful authentication.

## Overview

The application utilizes Python 3.10 and the Flask framework for the backend, with Flask templates for rendering HTML on the frontend. Authentication is managed through the Google OAuth2 API, with the application structured around Flask Blueprints to modularize the authentication flow. Configuration is handled via environment variables stored in a `.env` file, including Google API credentials and a Flask secret key.

## Features

- **User Authentication with Google:** Users can authenticate using their Google account.
- **Display User Information:** Upon successful authentication, the application displays the user's email and token.
- **Modular Architecture:** Utilizes Flask Blueprints for a clean and modular architecture.

## Getting started

### Requirements

- Python 3.10
- Flask
- A Google Cloud account with OAuth 2.0 credentials

### Quickstart

1. Clone the repository to your local machine.
2. Install the required Python packages: `pip install flask flask-dance python-dotenv flask-bootstrap`.
3. Create a `.env` file in the root directory with your Google client ID, client secret, Flask secret key, and callback URL.
4. Run the application: `python app.py`.

### License

Copyright (c) 2024.