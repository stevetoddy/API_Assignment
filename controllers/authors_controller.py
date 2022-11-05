from flask import Blueprint, request
from init import db
from models.author import Author, AuthorSchema
from flask_jwt_extended import jwt_required
from controllers.auth_controller import authorise


authors_bp = Blueprint('author', __name__, url_prefix='/author')


# Get all authors (requires authentication)
@authors_bp.route('/', methods=['GET'])
@jwt_required()
def all_authors():
    stmt = db.select(Author)
    authors = db.session.scalars(stmt)
    return AuthorSchema(many=True).dump(authors)


# Get one author by ID (requires authentication)
@authors_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def one_author(id):
    stmt = db.select(Author).filter_by(id=id)
    author = db.session.scalar(stmt)
    if author:
        return AuthorSchema().dump(author)
    else:
        return {'error': f'No author with id {id}'}, 404

# # Get all books by author
# @authors_bp.route('/titles/<int:id>', methods=['GET'])
# # @jwt_required()
# def all_titles(id):
#     stmt = db.select(Author).filter_by(id=id)
#     author = db.session.scalar(stmt)
#     if author:
#         return AuthorSchema().dump(author)
#     else:
#         return {'error': f'No author with id {id}'}, 404

# Get one author by First Name (requires authentication)
@authors_bp.route('first_name/<string:name>/', methods=['GET'])
@jwt_required()
def author_first_name(name):
    stmt = db.select(Author).filter_by(first_name=name)
    author = db.session.scalar(stmt)
    if author:
        return AuthorSchema().dump(author)
    else:
        return {'error': f'No author with the first name {name}'}, 404


# Get one author by Last Name (requires authentication)
@authors_bp.route('last_name/<string:name>/', methods=['GET'])
@jwt_required()
def author_last_name(name):
    stmt = db.select(Author).filter_by(last_name=name)
    author = db.session.scalar(stmt)
    if author:
        return AuthorSchema().dump(author)
    else:
        return {'error': f'No author with the last name {name}'}, 404


# Create author (need to be admin)
@authors_bp.route('/', methods=['POST'])
@jwt_required()
def create_author():
    # Checking if user has admin rights
    authorise()

    author = Author(
        first_name = request.json['first_name'],
        last_name = request.json['last_name'],
        accolades = request.json['accolades'],
        about = request.json['about']
    )
    # Add and commit author to database
    db.session.add(author)
    db.session.commit()

    # Respond to client
    return AuthorSchema().dump(author), 201


# Update an author by ID (need to be admin)
@authors_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_author(id):   
    # Checking if user has admin rights
    authorise()

    stmt = db.select(Author).filter_by(id=id)
    author = db.session.scalar(stmt)
    if author:
        author.first_name = request.json.get('first_name') or author.first_name
        author.last_name  = request.json.get('last_name') or author.last_name
        author.accolades  = request.json.get('accolades') or author.accolades
        author.about  = request.json.get('about') or author.about
        
        db.session.commit()
        return AuthorSchema().dump(author)
    else:
        return {'error': f'No author with id {id}'}, 404


# Delete a author by ID (need to be admin)
@authors_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_author(id):
    # Checking if user has admin rights
    authorise()

    stmt = db.select(Author).filter_by(id=id)
    author = db.session.scalar(stmt)
    if author:
        db.session.delete(author)
        db.session.commit()
        return {'message': f"Author '{author.first_name} {author.last_name}' deleted successfully"}
    else:
        return {'error': f'No author with id {id}'}, 404
        