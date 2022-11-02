from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Function to define our app
def create_app():
    app = Flask(__name__)

    # Getting our database link from our environment variables 
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    db = SQLAlchemy(app)

    @app.route('/')
    def index():
        return 'Hey'

    return app