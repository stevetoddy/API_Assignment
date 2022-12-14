from flask import Blueprint, request
from init import db
from models.author import Author, AuthorSchema
from flask_jwt_extended import jwt_required
from controllers.auth_controller import authorise

# Authors Blueprint
authors_bp = Blueprint('author', __name__, url_prefix='/author')


# Get all authors (requires authentication)
@authors_bp.route('/', methods=['GET'])
@jwt_required()
def all_authors():

    # Query to get all authors
    stmt = db.select(Author)
    authors = db.session.scalars(stmt)
    
    # Respond to client with all authors
    return AuthorSchema(many=True).dump(authors)


# Get one author by ID (requires authentication)
@authors_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def one_author(id):
    
    # Query to find author by ID
    stmt = db.select(Author).filter_by(id=id)
    author = db.session.scalar(stmt)
    
    # If found
    if author:
        
        # Respond to client with author
        return AuthorSchema().dump(author)
    
    # If not found
    else:
        return {'error': f'No author with id {id}'}, 404


# Get one author by First Name (requires authentication)
@authors_bp.route('first_name/<string:name>/', methods=['GET'])
@jwt_required()
def author_first_name(name):   
     
    # Query to find author by first name
    stmt = db.select(Author).filter_by(first_name=name)
    author = db.session.scalars(stmt)
    
    # If found
    if author:

        # Respond to client with author
        return AuthorSchema(many=True).dump(author)
    
    # If not found
    else:
        return {'error': f'No author with the first name {name}'}, 404


# Get one author by Last Name (requires authentication)
@authors_bp.route('last_name/<string:name>/', methods=['GET'])
@jwt_required()
def author_last_name(name):
         
    # Query to find author by last name
    stmt = db.select(Author).filter_by(last_name=name)
    author = db.session.scalars(stmt)
    
    # If found
    if author:
        
        # Respond to client with Author
        return AuthorSchema(many=True).dump(author)
    
    # If not found
    else:
        return {'error': f'No author with the last name {name}'}, 404


# Create author (need to be admin)
@authors_bp.route('/', methods=['POST'])
@jwt_required()
def create_author():
    # Checking if user has admin rights
    authorise()

    # Loading requests through schema for validation 
    data = AuthorSchema().load(request.json)
    
    author = Author(
        first_name = data['first_name'],
        last_name = data['last_name'],
        accolades = data.get('accolades'),
        about = data.get('about')
    )

    # Add and commit author to database
    db.session.add(author)
    db.session.commit()

    # Respond to client with new author
    return AuthorSchema().dump(author), 201


# Update an author by ID (need to be admin)
@authors_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_author(id):   
    # Checking if user has admin rights
    authorise()

    # Loading requests through schema for validation 
    data = AuthorSchema().load(request.json, partial=True)

    # Query to find author by ID
    stmt = db.select(Author).filter_by(id=id)
    author = db.session.scalar(stmt)
    
    # If found, update author with details sent
    if author:
        author.first_name = data.get('first_name') or author.first_name
        author.last_name  = data.get('last_name') or author.last_name
        author.accolades  = data.get('accolades') or author.accolades
        author.about  = data.get('about') or author.about
        
        # Commit changes to database
        db.session.commit()
        
        # Respond to client with updated author
        return AuthorSchema().dump(author)
    
    # If not found
    else:
        return {'error': f'No author with id {id}'}, 404


# Delete a author by ID (need to be admin)
@authors_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_author(id):
    # Checking if user has admin rights
    authorise()
         
    # Query to find author by ID
    stmt = db.select(Author).filter_by(id=id)
    author = db.session.scalar(stmt)
    
    # If found
    if author:

        # Delete Author and commit changes to database
        db.session.delete(author)
        db.session.commit()

        # Respond to client
        return {'message': f"Author '{author.first_name} {author.last_name}' deleted successfully"}
    
    # If not found
    else:
        return {'error': f'No author with id {id}'}, 404
        