from flask import Flask
from init import db, ma
from flask_sqlalchemy import SQLAlchemy
from controllers.books_controller import books_bp
from models.book import Book, BookSchema
import os

# Function to define our app
def create_app():
    app = Flask(__name__)

    # Getting our database link from our environment variables 
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    
    # Stopping Flask from trying to sort the returned JSON resources 
    app.config['JSON_SORT_KEYS'] = False

    db.init_app(app)
    ma.init_app(app)

    # Connecting Blueprints to app
    app.register_blueprint(books_bp)

    # @app.cli.command('create')
    # def create_db():
    #     db.create_all()
    #     print("Tables created")

    @app.cli.command('seed')
    def seed_db():
        books = [
            Book(
                title = 'Name of the wind',
                is_fiction = True,
                is_kid_friendly = False,
                in_store = 0
            ),
            Book(
                title = 'The Wise Man\'s Fear',
                is_fiction = True,
                is_kid_friendly = False,
                in_store = 2
            ),
            Book(
                title = 'The Way of Kings',
                is_fiction = True,
                is_kid_friendly = False,
                in_store = 4
            ),
            Book(
                title = 'Catch 22',
                is_fiction = True,
                is_kid_friendly = False,
                in_store = 2
            ),
            Book(
                title = 'Cat in the Hat',
                is_fiction = True,
                is_kid_friendly = True,
                in_store = 5
            ),
            Book(
                title = 'Oxford English Dictionary',
                is_fiction = False,
                is_kid_friendly = True,
                in_store = 9
            )
        ]

        db.session.add_all(books)
        db.session.commit()

    print('Tables seeded')
    
    # Must return the app so Flask can recognise it 
    return app