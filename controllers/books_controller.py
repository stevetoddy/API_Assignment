from flask import Blueprint, request
from init import db, ma
from models.book import Book, BookSchema

books_bp = Blueprint('books', __name__, url_prefix='/books')

# Get all books
@books_bp.route('/', methods=['GET'])
def all_books():
    stmt = db.select(Book)
    books = db.session.scalars(stmt)
    return BookSchema(many=True).dump(books)

# Get one book by ID
@books_bp.route('/<int:id>', methods=['GET'])
def one_book(id):
    stmt = db.select(Book).filter_by(id=id)
    book = db.session.scalar(stmt)
    if book:
        return BookSchema().dump(book)
    else:
        return {'error': f'No book with id {id}'}, 404

# Get one book by Title
@books_bp.route('/title/<string:title>', methods=['GET'])
def title_book(title):
    stmt = db.select(Book).filter_by(title=title)
    book = db.session.scalar(stmt)
    if book:
        return BookSchema().dump(book)
    else:
        return {'error': f'No book with the title {title}'}, 404

# Create books
@books_bp.route('/', methods=['POST'])
def create_book():
    book = Book(
        title = request.json['title'],
        is_fiction = request.json['is_fiction'],
        is_kid_friendly  = request.json['is_kid_friendly'],
        in_store = request.json['in_store']
    )
    # Add and commit book to database
    db.session.add(book)
    db.session.commit()

    # Respond to client
    return BookSchema().dump(book), 201

# Update a book by ID
@books_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update_one_book(id):
    stmt = db.select(Book).filter_by(id=id)
    book = db.session.scalar(stmt)
    if book:
        book.title = request.json.get('title') or book.title
        book.is_fiction  = request.json.get('is_fiction') or book.is_fiction

        # if book.is_fiction is not None: 
        #     book.is_fiction = request.json.get('is_fiction') 
        # # elif book.is_fiction != "1":
        # #     book.is_fiction = request.json.get('is_fiction')
        # else: 
        #     book.is_fiction

        book.is_kid_friendly  = request.json.get('is_kid_friendly') or book.is_kid_friendly
        book.in_store = request.json.get('in_store') or book.in_store
        db.session.commit()
        return BookSchema().dump(book)
    else:
        return {'error': f'No book with id {id}'}, 404


# Delete a book by ID
@books_bp.route('/<int:id>', methods=['DELETE'])
def delete_one_book(id):
    stmt = db.select(Book).filter_by(id=id)
    book = db.session.scalar(stmt)
    if book:
        db.session.delete(book)
        db.session.commit()
        return {'message': 'Book deleted successfully'}
    else:
        return {'error': f'No book with id {id}'}, 404