from flask import Flask
from init import db, ma
import os

def create_app():
    # Instantiating our Flask app as app
    app = Flask(__name__)

    # Getting the Database URI from my global variables file to link database
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    # Pulling db from init.py to instantiate the SQLAlchemy db model and passing in our flask app 
    db.init_app(app)
    ma.init_app(app)