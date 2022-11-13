from flask import Blueprint
from init import db, bc
from models.book import Book
from models.user import User
from models.comment import Comment
from models.author import Author
from models.category import Category 


db_commands = Blueprint('db', __name__)

# Create the database
@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")

# Drop the database
@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

# Seed database with dummy info
@db_commands.cli.command('seed')
def seed_db():
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
            about = 'Brandon Sanderson is an American author of epic fantasy and science fiction.'
        ),        
        Author(
            first_name = 'Dr',
            last_name = 'Seuss',
            accolades = 'His work includes many of the most popular children\'s books of all time, selling over 600 million copies and being translated into more than 20 languages by the time of his death.',
            about = 'Theodor Seuss Geisel was an American children\'s author and cartoonist.'
        ),        
        Author(
            first_name = 'Joseph',
            last_name = 'Heller',
            accolades = 'Although Catch-22 won no awards, it has remained consistently in print and, since publication, has sold more than 10m copies.',
            about = 'Joseph Heller was an American author of novels, short stories, plays, and screenplays. His best-known work is the 1961 novel Catch-22.'
        ),
        Author(
            first_name = 'Iain',
            last_name = 'Banks',
            accolades = 'Iain has been nominated for Hugo, Arthur C. Clark, Prometheus and Goodreads awards among others',
            about = 'Iain Banks was a Scottish author, writing mainstream fiction as Iain Banks and science fiction as Iain M. Banks.'
        ),
        Author(
            first_name = 'Al',
            last_name = 'Sweigart',
            accolades = 'Sweigart has written several bestselling programming books for beginners, including Automate the Boring Stuff with Python.',
            about = 'Al Sweigart is a professional software developer who teaches programming to kids and adults.'
        )
        ]
    # Add and commit all seeded authors
    db.session.add_all(authors)
    db.session.commit()

    categories = [
        Category(
            name = 'Fantasy',
            description = 'Imaginative fiction dependent for effect on strangeness of setting (such as other worlds or times) and of characters (such as supernatural or unnatural beings).'
        ),
        Category(
            name = 'Sci-Fi',
            description = 'Science fiction, also often known as "sci-fi", is a genre of literature that is imaginative and based around science. It relies heavily on scientific facts, theories, and principles as support for its settings, characters, themes, and plot.'
        ),        
        Category(
            name = 'Children',
            description = 'Children\'s books are everything from Young Adult down to board books for your teething kiddo, however, a book is considered a children\'s book when it\'s intended for an audience between 0-8 years old.'
        ),        
        Category(
            name = 'Satirical',
            description = 'Satire in literature is a type of social commentary. Writers use exaggeration, irony, and other devices to poke fun of a particular leader, a social custom or tradition, or any other prevalent social figure or practice that they want to comment on and call into question.'
        ),
        Category(
            name = 'Educational',
            description = 'Books in the education nonfiction genre can either be books about forms of education and how it\'s achieved or be educational itself, in the form of text books and educational materials.'
        )
        ]
    # Add and commit all seeded categories
    db.session.add_all(categories)
    db.session.commit()
    

    books = [
        Book(
            title = 'The Name of the Wind',
            is_fiction = True,
            in_store = 0,
            author = authors[0],
            category = categories[0]
        ),
        Book(
            title = 'The Wise Man\'s Fear',
            is_fiction = True,
            in_store = 2,
            author = authors[0],
            category = categories[0]
        ),
        Book(
            title = 'The Way of Kings',
            is_fiction = True,
            in_store = 4,
            author = authors[1],
            category = categories[0]
        ),
        Book(
            title = 'Catch 22',
            is_fiction = True,
            in_store = 2,
            author = authors[3],
            category = categories[3]
        ),
        Book(
            title = 'Excession',
            is_fiction = True,
            in_store = 3,
            author = authors[4],
            category = categories[1]
        ),
        Book(
            title = 'Cat in the Hat',
            is_fiction = True,
            in_store = 5,
            author = authors[2],
            category = categories[2]
        ),
        Book(
            title = 'Automate the Boring Stuff with Python',
            is_fiction = False,
            in_store = 1,
            author = authors[5],
            category = categories[4]
        )
        ]
    # Add and commit all seeded books
    db.session.add_all(books)
    db.session.commit()

    users = [
        User(
            email = 'steve@email.com',
            password=bc.generate_password_hash('12345Aa!').decode('utf-8'),
            first_name = 'Steve',
            last_name = 'Todorovic',
            is_admin = True
        ),        
        User(
            email = 'denna@email.com',
            password=bc.generate_password_hash('12345Aa!').decode('utf-8'),
            first_name = 'Denna',
            last_name = 'Thomas',
            is_admin = False
        ),
        User(
            email = 'bast@email.com',
            password=bc.generate_password_hash('12345Aa!').decode('utf-8'),
            first_name = 'Sebastian',
            last_name = 'Townsend',
            is_admin = False
        ),
        User(
            email = 'ben@email.com',
            password=bc.generate_password_hash('12345Aa!').decode('utf-8'),
            first_name = 'Ben',
            last_name = 'Abenathy',
            is_admin = False
        ),
        User(
            email = 'sim@email.com',
            password=bc.generate_password_hash('12345Aa!').decode('utf-8'),
            first_name = 'Simon',
            last_name = 'Williams',
            is_admin = False
        ),
        ]
    # Add and commit all seeded users
    db.session.add_all(users)
    db.session.commit()


    comments = [
        Comment(
            body = 'Name of the Wind is a fantastic take on the young hero trope',
            user = users[1],
            book = books[0]
        ),
        Comment(
            body = 'Book 2 of 3 in The Kingkiller Chronicles',
            user = users[0],
            book = books[1]
        ),        
        Comment(
            body = 'The first book in Sanderson\'s epic Stormlight Archive series',
            user = users[2],
            book = books[2]
        ),        
        Comment(
            body = 'Hilarious and harrowing at the same time!',
            user = users[2],
            book = books[3]
        ),
        Comment(
            body = 'Sci-Fi on a massive scale, will leave you think',
            user = users[3],
            book = books[4]
        )
        ]
    # Add and commit all seeded categories
    db.session.add_all(comments)
    db.session.commit()


    print('Tables seeded')