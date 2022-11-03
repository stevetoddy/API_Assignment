from flask import Flask
from init import db, ma
from flask_sqlalchemy import SQLAlchemy
from controllers.books_controller import books_bp
from controllers.users_controller import users_bp
from controllers.authors_controller import authors_bp
from controllers.cli_controller import db_commands
from models.book import Book, BookSchema
import os

# Function to define our app
def create_app():
    app = Flask(__name__)

    # Error handlers 
    @app.errorhandler(400)
    def bad_request(err):
        return {"error": str(err)}, 400
    
    @app.errorhandler(404)
    def not_found(err):
        return {"error": str(err)}, 404

    @app.errorhandler(405)
    def method_not_allowed(err):
        return {"error": str(err)}, 405

    # Getting our database link from our environment variables 
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    
    # Stopping Flask from trying to sort the returned JSON resources 
    app.config['JSON_SORT_KEYS'] = False

    db.init_app(app)
    ma.init_app(app)

    # Connecting Blueprints to app
    app.register_blueprint(books_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(authors_bp)
    app.register_blueprint(db_commands)

    
    # Must return the app so Flask can recognise it 
    return app