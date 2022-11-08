from flask import Blueprint, request
from init import db
from models.user import User, UserSchema
from flask_jwt_extended import jwt_required
from controllers.auth_controller import authorise

# Users Blueprint
users_bp = Blueprint('users', __name__, url_prefix='/users')


# Get all users (requires authentication)
@users_bp.route('/', methods=['GET'])
@jwt_required()
def all_users():
   
    # Query
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    
    # Respond to client
    return UserSchema(many=True, exclude=['password']).dump(users)


# Get one user by ID (requires authentication)
@users_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def one_user(id):

    # Query
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
   
    # If found
    if user:
        
        # Respond to client
        return UserSchema(exclude=['password']).dump(user)
    
    # If not found
    else:
        return {'error': f'No user with id {id}'}, 404


# Get one user by First Name (requires authentication)
@users_bp.route('first_name/<string:name>/', methods=['GET'])
@jwt_required()
def user_first_name(name):

    # Query
    stmt = db.select(User).filter_by(first_name=name)
    user = db.session.scalar(stmt)
    
    # If found
    if user:

        # Respond to client
        return UserSchema(exclude=['password']).dump(user)
   
    # If not found
    else:
        return {'error': f'No user with the first name {name}'}, 404


# Get one user by Last Name (requires authentication)
@users_bp.route('last_name/<string:name>/', methods=['GET'])
@jwt_required()
def user_last_name(name):

    # Query
    stmt = db.select(User).filter_by(last_name=name)
    user = db.session.scalar(stmt)
    
    # If found
    if user:

        # Respond to client
        return UserSchema(exclude=['password']).dump(user)
    
    # If not found
    else:
        return {'error': f'No user with the last name {name}'}, 404


# Update a User by ID (need admin rights)
@users_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_user(id):
    # Checking if user has admin rights
    authorise()
    
    # Loading requests through schema for validation 
    data = UserSchema().load(request.json)
    
    # Query
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    
    # If found
    if user:
        user.email = data.get('email') or user.email
        user.password  = data.get('password') or user.password
        user.first_name = data.get('first_name') or user.first_name
        user.last_name  = data.get('last_name') or user.last_name
        # Try block for Boolean values
        try:
            user.is_admin =data['is_admin'] 
        except:
            user.is_admin = user.is_admin
        
        # Commit User changes to database
        db.session.commit()
        
        # Respond to client
        return UserSchema(exclude=['password']).dump(user)
    
    # If not found
    else:
        return {'error': f'No user with id {id}'}, 404


# Delete a user by ID (need to be admin)
@users_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    # Checking if user has admin rights
    authorise()
    
    # Query
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    
    # If found
    if user:

        # Delete and commit changes to database
        db.session.delete(user)
        db.session.commit()
    
        # Respond to client
        return {'message': f"User '{user.first_name} {user.last_name}' deleted successfully"}
    
    # If not found
    else:
        return {'error': f'No user with id {id}'}, 404