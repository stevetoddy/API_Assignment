from flask import Blueprint, request
from init import db
from models.user import User, UserSchema
from flask_jwt_extended import jwt_required
from controllers.auth_controller import authorise


users_bp = Blueprint('users', __name__, url_prefix='/users')


# Get all users (requires authentication)
@users_bp.route('/', methods=['GET'])
@jwt_required()
def all_users():
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return UserSchema(many=True, exclude=['password']).dump(users)


# Get one user by ID (requires authentication)
@users_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def one_user(id):
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema(exclude=['password']).dump(user)
    else:
        return {'error': f'No user with id {id}'}, 404


# Get one user by First Name (requires authentication)
@users_bp.route('first_name/<string:name>/', methods=['GET'])
@jwt_required()
def user_first_name(name):
    stmt = db.select(User).filter_by(first_name=name)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema(exclude=['password']).dump(user)
    else:
        return {'error': f'No user with the first name {name}'}, 404


# Get one user by Last Name (requires authentication)
@users_bp.route('last_name/<string:name>/', methods=['GET'])
@jwt_required()
def user_last_name(name):
    stmt = db.select(User).filter_by(last_name=name)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema(exclude=['password']).dump(user)
    else:
        return {'error': f'No user with the last name {name}'}, 404


# Update a User by ID (need admin rights)
@users_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_user(id):
    # Checking if user has admin rights
    if not authorise():
        return {"error":"Must be admin to preform this action"}, 401

    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        user.email = request.json.get('email') or user.email
        user.first_name = request.json.get('first_name') or user.first_name
        user.last_name  = request.json.get('last_name') or user.last_name
        # Try block for Boolean values
        try:
            user.is_admin = request.json['is_admin'] 
        except:
            user.is_admin = user.is_admin
        
        db.session.commit()
        return UserSchema(exclude=['password']).dump(user)
    else:
        return {'error': f'No user with id {id}'}, 404


# Delete a user by ID (need to be admin)
@users_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    # Checking if user has admin rights
    if not authorise():
        return {"error":"Must be admin to preform this action"}, 401

    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message': f"User '{user.first_name} {user.last_name}' deleted successfully"}
    else:
        return {'error': f'No user with id {id}'}, 404