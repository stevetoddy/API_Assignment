from flask import Blueprint, request
from init import db
from models.book import Book, BookSchema
from models.comment import Comment, CommentSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.auth_controller import authorise
# from boolean_try_block import boolean_try


books_bp = Blueprint('books', __name__, url_prefix='/books')


# Get all books (requires authentication)
@books_bp.route('/', methods=['GET'])
@jwt_required()
def all_books():
    stmt = db.select(Book)
    books = db.session.scalars(stmt)
    return BookSchema(many=True).dump(books)


# Get one book by ID (requires authentication)
@books_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def one_book(id):
    stmt = db.select(Book).filter_by(id=id)
    book = db.session.scalar(stmt)
    print(book)
    print(stmt)
    if book:
        return BookSchema().dump(book)
    else:
        return {'error': f'No book with id {id}'}, 404


# Get all books by Author (requires authentication)
@books_bp.route('/author/<int:author_id>', methods=['GET'])
@jwt_required()
def author_books(author_id):
    stmt = db.select(Book).filter_by(author_id=author_id)
    book = db.session.scalars(stmt)
    if book:
        return BookSchema(many=True, exclude=['comments']).dump(book)
    else:
        return {'error': f'No author with id {author_id}'}, 404
        

# Get all books by Category (requires authentication)
@books_bp.route('/category/<int:category_id>', methods=['GET'])
@jwt_required()
def category_books(category_id):
    stmt = db.select(Book).filter_by(category_id=category_id)
    book = db.session.scalars(stmt)
    if book:
        return BookSchema(many=True, exclude=['comments']).dump(book)
    else:
        return {'error': f'No category with id {category_id}'}, 404


# Get one book by Title  (requires authentication)
@books_bp.route('/<string:title>', methods=['GET'])
@jwt_required()
def title_book(title):
    stmt = db.select(Book).filter_by(title=title)
    book = db.session.scalar(stmt)
    if book:
        return BookSchema().dump(book)
    else:
        return {'error': f'No book with the title {title}'}, 404


# Create books (requires authentication)
@books_bp.route('/', methods=['POST'])
@jwt_required()
def create_book():
    book = Book(
        title = request.json['title'],
        is_fiction = request.json['is_fiction'],
        is_kid_friendly  = request.json['is_kid_friendly'],
        in_store = request.json['in_store'],
        author_id = request.json['author_id'],
        category_id = request.json['category_id']
    )

    db.session.add(book)
    db.session.commit()

    return BookSchema().dump(book), 201


# Create comments (requires authentication)
@books_bp.route('<int:id>/comment/', methods=['POST'])
@jwt_required()
def create_comment(id):
    comment = Comment(
        body = request.json['body'],
        user_id = get_jwt_identity(),
        book_id = id
    )

    db.session.add(comment)
    db.session.commit()

    return CommentSchema().dump(comment), 201


# Update a book by ID (need to be admin)
@books_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_book(id):
    # Checking if user has admin rights
    authorise()

    stmt = db.select(Book).filter_by(id=id)
    book = db.session.scalar(stmt)
    if book:
        book.title = request.json.get('title') or book.title
        
        # boolean_try(book.is_fiction, 'is_fiction')

        # Try block for Boolean values
        try:
            book.is_fiction = request.json['is_fiction'] 
        except:
            book.is_fiction = book.is_fiction
        # Try block for Boolean values
        try:
            book.is_kid_friendly  = request.json['is_kid_friendly']
        except:
            book.is_kid_friendly = book.is_kid_friendly

        book.in_store = request.json.get('in_store') or book.in_store
        
        db.session.commit()
        
        return BookSchema().dump(book)

    else:
        return {'error': f'No book with id {id}'}, 404


# Delete a book by ID (need to be admin)
@books_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_one_book(id):

    # Checking if user has admin rights
    authorise()

    stmt = db.select(Book).filter_by(id=id)
    book = db.session.scalar(stmt)
    if book:
        db.session.delete(book)
        db.session.commit()
        return {'message': f"Book '{book.title}' deleted successfully"}
    else:
        return {'error': f'No book with id {id}'}, 404
        