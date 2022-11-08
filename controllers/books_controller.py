from flask import Blueprint, request
from init import db
from models.book import Book, BookSchema
from models.comment import Comment, CommentSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.auth_controller import authorise

# Books Blueprint
books_bp = Blueprint('books', __name__, url_prefix='/books')


# Get all books (requires authentication)
@books_bp.route('/', methods=['GET'])
@jwt_required()
def all_books():
    
    # Query to get all books
    stmt = db.select(Book)
    books = db.session.scalars(stmt)

    # Respond to client with all books 
    return BookSchema(many=True).dump(books)


# Get one book by ID (requires authentication)
@books_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def one_book(id):

    # Query to find book by ID
    stmt = db.select(Book).filter_by(id=id)
    book = db.session.scalar(stmt)

    # If found
    if book:

        # Respond to client with book
        return BookSchema().dump(book)
    
    # If not found
    else:
        return {'error': f'No book with id {id}'}, 404


# Get all books by Author (requires authentication)
@books_bp.route('/author/<int:author_id>', methods=['GET'])
@jwt_required()
def author_books(author_id):
    
    # Query to find book by Author ID
    stmt = db.select(Book).filter_by(author_id=author_id)
    book = db.session.scalars(stmt)

    # If found
    if book:
        
        # Respond to client with book excluding linked comments 
        return BookSchema(many=True, exclude=['comments']).dump(book)
    
    # If not found
    else:
        return {'error': f'No author with id {author_id}'}, 404
        

# Get all books by Category (requires authentication)
@books_bp.route('/category/<int:category_id>', methods=['GET'])
@jwt_required()
def category_books(category_id):
    
    # Query to find book by Category ID
    stmt = db.select(Book).filter_by(category_id=category_id)
    book = db.session.scalars(stmt)
    
    # If found
    if book:
        
        # Respond to client with book excluding linked comments
        return BookSchema(many=True, exclude=['comments']).dump(book)
    
    # If not found
    else:
        return {'error': f'No category with id {category_id}'}, 404


# Get one book by Title  (requires authentication)
@books_bp.route('/<string:title>', methods=['GET'])
@jwt_required()
def title_book(title):

    # Query to find book by title
    stmt = db.select(Book).filter_by(title=title)
    book = db.session.scalar(stmt)
   
    # If found
    if book:
        
        # Respond to client with book
        return BookSchema().dump(book)
    
    # If not found
    else:
        return {'error': f'No book with the title {title}'}, 404


# Create books (requires authentication)
@books_bp.route('/', methods=['POST'])
@jwt_required()
def create_book():

    # Loading requests through schema for validation 
    data = BookSchema().load(request.json)

    book = Book(
        title = data['title'],
        is_fiction = data['is_fiction'],
        is_kid_friendly  = data['is_kid_friendly'],
        in_store = data['in_store'],
        author_id = data['author_id'],
        category_id = data['category_id']
    )

    # Add new book and commit to database
    db.session.add(book)
    db.session.commit()

    # Respond to client with new book
    return BookSchema().dump(book), 201


# Create comments (requires authentication)
@books_bp.route('<int:id>/comment/', methods=['POST'])
@jwt_required()
def create_comment(id):

    # Loading requests through schema for validation 
    data = CommentSchema().load(request.json)

    # Query to find book by ID
    stmt = db.select(Book).filter_by(id=id)
    book = db.session.scalar(stmt)

    # If found, create comment
    if book:
        comment = Comment(
            body = data['body'],
            user_id = get_jwt_identity(),
            book_id = id
        )

        # Add and commit comment to database
        db.session.add(comment)
        db.session.commit()

        # Respond to client with new comment 
        return CommentSchema().dump(comment), 201
    
    # If not found
    else:
        return {"error": f"No book found with id {id}"}


# Update a book by ID (need to be admin)
@books_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_book(id):
    # Checking if user has admin rights
    authorise()

    # Loading requests through schema for validation 
    data = CommentSchema().load(request.json)

    # Query to find book by ID
    stmt = db.select(Book).filter_by(id=id)
    book = db.session.scalar(stmt)

    # If found, update book with details sent
    if book:
        book.title = data.get('title') or book.title
        # Try block for Boolean values
        try:
            book.is_fiction = data['is_fiction'] 
        except:
            book.is_fiction = book.is_fiction
        # Try block for Boolean values
        try:
            book.is_kid_friendly  = data['is_kid_friendly']
        except:
            book.is_kid_friendly = book.is_kid_friendly

        book.in_store = data.get('in_store') or book.in_store
        
        # Commit changes to database
        db.session.commit()
        
        # Respond to client with updated book
        return BookSchema().dump(book)

    # If not found
    else:
        return {'error': f'No book with id {id}'}, 404


# Delete a book by ID (need to be admin)
@books_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_one_book(id):

    # Checking if user has admin rights
    authorise()

    # Query to find book by ID
    stmt = db.select(Book).filter_by(id=id)
    book = db.session.scalar(stmt)

    # If found
    if book:

        # Delete and commit changes to database
        db.session.delete(book)
        db.session.commit()

        # Respond to client
        
        return {'message': f"Book '{book.title}' deleted successfully"}
    #If not found
    else:
        return {'error': f'No book with id {id}'}, 404
        