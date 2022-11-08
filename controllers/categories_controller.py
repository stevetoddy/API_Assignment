from flask import Blueprint, request
from init import db
from models.category import Category, CategorySchema
from flask_jwt_extended import jwt_required
from controllers.auth_controller import authorise

# Categories Blueprint
categories_bp = Blueprint('categories', __name__, url_prefix='/categories')


# Get all categories (requires authentication)
@categories_bp.route('/', methods=['GET'])
@jwt_required()
def all_categories():
    
    # Query
    stmt = db.select(Category)
    categories = db.session.scalars(stmt)
    
    # Respond to client
    return CategorySchema(many=True).dump(categories)


# Get one category by ID (requires authentication)
@categories_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def one_category(id):

    # Query
    stmt = db.select(Category).filter_by(id=id)
    category = db.session.scalar(stmt)
    
    # If found
    if category:

        # Respond to client
        return CategorySchema().dump(category)
    
    # If not found
    else:
        return {'error': f'No category with id {id}'}, 404


# Get category by Name (requires authentication)
@categories_bp.route('/<string:name>/', methods=['GET'])
@jwt_required()
def category_name(name):
    
    # Query
    stmt = db.select(Category).filter_by(name=name)
    category = db.session.scalar(stmt)
    
    # If found
    if category:
        
        # Respond to client
        return CategorySchema().dump(category)
    
    # If not found
    else:
        return {'error': f'No category called {name}'}, 404


# Create categories (need to be admin)
@categories_bp.route('/', methods=['POST'])
@jwt_required()
def create_category():
    # Checking if user has admin rights
    authorise()
    # Loading requests through schema for validation 
    data = CategorySchema().load(request.json)
    
    category = Category(
        name = data['name'],
        description = data['description']
    )

    # Add and commit author to database
    db.session.add(category)
    db.session.commit()

    # Respond to client
    return CategorySchema().dump(category), 201


# Update a category by ID (need to be admin)
@categories_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_category(id):
    # Checking if user has admin rights
    authorise()
    
    # Loading requests through schema for validation 
    data = CategorySchema().load(request.json)
    
    # Query
    stmt = db.select(Category).filter_by(id=id)
    category = db.session.scalar(stmt)
    
    # If found
    if category:
        category.name = data.get('name') or category.name
        category.description  = data.get('description') or category.description
        
        # Commit author updates to database
        db.session.commit()
    
        # Respond to client
        return CategorySchema().dump(category)
    
    # If not found
    else:
        return {'error': f'No category with id {id}'}, 404


# Delete a category by ID (need to be admin)
@categories_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_category(id):
    # Checking if user has admin rights
    authorise()

    # Query
    stmt = db.select(Category).filter_by(id=id)
    category = db.session.scalar(stmt)
   
    # If found
    if category:

        # Delete and commit changes to database
        db.session.delete(category)
        db.session.commit()

        # Respond to client
        return {'message': f"Category '{category.name}' deleted successfully"}
   
    # If not found
    else:
        return {'error': f'No category with id {id}'}, 404
        