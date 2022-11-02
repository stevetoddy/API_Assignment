from flask import Blueprint
from init import db, ma
from models.book import Book, BookSchema

books_bp = Blueprint('books', __name__, url_prefix='/books')

@books_bp.route('/', methods=['GET'])
def all_books():
    # return "books route"
    stmt = db.select(Book)
    books = db.session.scalars(stmt)
    return BookSchema(many=True).dump(books)

# Get one book by ID
@books_bp.route('/<int:id>', methods=['GET'])
def one_book(id):
    stmt = db.select(Book).filter_by(id=id)
    book = db.session.scalar(stmt)
    return BookSchema().dump(book)

# Get one book by Title DOESN'T WORK YET!
# @books_bp.route('/title/<title>', methods=['GET'])
# def title_book(title):
#     stmt = db.select(Book).filter_by(title=title)
#     book = db.session.scalars(stmt)
#     return BookSchema(many=True).dump(book)
    