from flask import Blueprint, request
from init import db
from models.user import User, UserSchema


users_bp = Blueprint('users', __name__, url_prefix='/users')


# Get all users
@users_bp.route('/', methods=['GET'])
def all_users():
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return UserSchema(many=True).dump(users)


# Get one user by ID
@users_bp.route('/<int:id>', methods=['GET'])
def one_user(id):
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema().dump(user)
    else:
        return {'error': f'No user with id {id}'}, 404


# Get one user by First Name
@users_bp.route('first_name/<string:name>/', methods=['GET'])
def user_first_name(name):
    stmt = db.select(User).filter_by(first_name=name)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema().dump(user)
    else:
        return {'error': f'No user with the first name {name}'}, 404


# Get one user by Last Name
@users_bp.route('last_name/<string:name>/', methods=['GET'])
def user_last_name(name):
    stmt = db.select(User).filter_by(last_name=name)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema().dump(user)
    else:
        return {'error': f'No user with the last name {name}'}, 404


# Create users
@users_bp.route('/', methods=['POST'])
def create_user():
    user = User(
        email = request.json['email'],
        first_name = request.json['first_name'],
        last_name = request.json['last_name'],
        is_admin = request.json['is_admin']
    )

    db.session.add(user)
    db.session.commit()

    return UserSchema().dump(user), 201


# Update a User by ID
@users_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update_user(id):
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
        return UserSchema().dump(user)
    else:
        return {'error': f'No user with id {id}'}, 404


# Delete a user by ID
@users_bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message': f"User '{user.first_name} {user.last_name}' deleted successfully"}
    else:
        return {'error': f'No user with id {id}'}, 404