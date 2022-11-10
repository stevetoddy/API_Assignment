from flask import Flask, abort
from init import db, ma, bc, jwt
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import StatementError
from controllers.books_controller import books_bp
from controllers.users_controller import users_bp
from controllers.authors_controller import authors_bp
from controllers.categories_controller import categories_bp
from controllers.comments_controller import comments_bp
from controllers.auth_controller import auth_bp
from controllers.cli_controller import db_commands
import os


# Function to define our app
def create_app():
    app = Flask(__name__)


    # Error handlers 
            
    @app.errorhandler(KeyError)
    def key_err(err):
        return {"error": f"Missing field: {str(err)}"}, 400
                
    @app.errorhandler(ValidationError)
    def validation_err(err):
        return {"error": err.messages}, 400
    
    @app.errorhandler(TypeError)
    def type_err(err):
        return {"error": str(err)}, 400

    @app.errorhandler(ValueError)
    def value_err(err):
        return {"error": str(err)}, 400
    
    @app.errorhandler(StatementError)
    def statement_err(err):
        return {"error": "Make sure all values are valid and of the correct type"}, 400

    @app.errorhandler(400)
    def bad_request(err):
        return {"error": str(err)}, 400
            
    @app.errorhandler(401)
    def not_authorised(err):
        return {"error": str(err)}, 401
    
    @app.errorhandler(404)
    def not_found(err):
        return {"error": str(err)}, 404

    @app.errorhandler(405)
    def method_not_allowed(err):
        return {"error": str(err)}, 405
        
    @app.errorhandler(409)
    def conflict_err(err):
        return {"error": str(err)}, 409


    # Getting our database link from our environment variables 
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    
    # Stopping Flask from trying to sort the returned JSON resources 
    app.config['JSON_SORT_KEYS'] = False

    # Getting JWT secret key from environment variables 
    app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET_KEY')

    # Instantiating modules 
    db.init_app(app)
    ma.init_app(app)
    bc.init_app(app)
    jwt.init_app(app)


    # Connecting Blueprints to app
    app.register_blueprint(books_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(authors_bp)
    app.register_blueprint(categories_bp)
    app.register_blueprint(comments_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(db_commands)

    
    # Must return the app so Flask can recognise it 
    return app