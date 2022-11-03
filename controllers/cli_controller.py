from flask import Blueprint
from init import db
from models.book import Book
from models.user import User
# from models.comment import Comment
from models.author import Author
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

    authors = [
        Author(
            first_name = 'Patrick',
            last_name = 'Rothfuss',
            accolades = 'Patrick has won several awards, including the 2007 Quill Award for his debut novel, The Name of the Wind. Its sequel, The Wise Man\'s Fear, topped The New York Times Best Seller list.',
            about = 'Patrick James Rothfuss is an American author. He is best known for his projected trilogy The Kingkiller Chronicle'
        ),
        Author(
            first_name = 'Brandon',
            last_name = 'Sanderson',
            accolades = 'Sanderson has been nominated for and also won multiple awards for his various works, including being nominated for four Hugo awards, winning one, and being nominated for 5 David Gemmell Legend Awards, winning two',
            about = 'Brandon Sanderson is an American author of epic fantasy and science fiction. He is best known for the Cosmere fictional universe, in which most of his fantasy novels, most notably the Mistborn series and The Stormlight Archive, are set.'
        ),        
        Author(
            first_name = 'Dr',
            last_name = 'Seuss',
            accolades = 'His work includes many of the most popular children\'s books of all time, selling over 600 million copies and being translated into more than 20 languages by the time of his death.',
            about = 'Theodor Seuss Geisel was an American children\'s author and cartoonist. He is known for his work writing and illustrating more than 60 books under the pen name Dr. Seuss. '
        ),        
        Author(
            first_name = 'Joseph',
            last_name = 'Heller',
            accolades = 'Although Catch-22 won no awards, it has remained consistently in print and, since publication, has sold more than 10m copies.',
            about = 'Joseph Heller was an American author of novels, short stories, plays, and screenplays. His best-known work is the 1961 novel Catch-22, a satire on war and bureaucracy, whose title has become a synonym for an absurd or contradictory choice.'
        ),
        ]
    # Add and commit all seeded authors
    db.session.add_all(authors)
    db.session.commit()

    print('Tables seeded')