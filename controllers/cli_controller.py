from flask import Blueprint
from init import db
from models.book import Book
from models.user import User
# from models.comment import Comment
# from models.author import Authors
# from models.category import Categories 


db_commands = Blueprint('db', __name__)

# Create the database
@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_db():
    books = [
        Book(
            title = 'The Name of the Wind',
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
    # Add and commit all seeded books
    db.session.add_all(books)
    db.session.commit()

    users = [
        User(
            first_name = 'Steve',
            last_name = 'Todorovic',
            is_admin = True
        ),        
        User(
            first_name = 'Denna',
            last_name = 'Thomas',
            is_admin = False
        ),
        User(
            first_name = 'Sebastian',
            last_name = 'Townsend',
            is_admin = False
        ),
        User(
            first_name = 'Ben',
            last_name = 'Abenathy',
            is_admin = False
        ),
        User(
            first_name = 'Simon',
            last_name = 'Williams',
            is_admin = False
        ),
        ]
    # Add and commit all seeded users
    db.session.add_all(users)
    db.session.commit()

    print('Tables seeded')