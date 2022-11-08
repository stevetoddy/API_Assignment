from flask import Blueprint, request, abort
from init import db, bc, jwt
from models.user import User, UserSchema
from sqlalchemy.exc import IntegrityError
from datetime import timedelta
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

# Auth Controller Blueprint
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


# Admin Authorisation function
def authorise():
    # Gets JWT Token from user accessing a route with admin authorisation required
    user_id = get_jwt_identity()

    # Query to find user with token
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)

    # If not admin abort action and throw error 401  
    if not user.is_admin:
        abort(401)


# Register a new user
@auth_bp.route('/register/', methods=['POST'])
@jwt_required()
def auth_register():
        
    # Loading requests through schema for validation 
    data = UserSchema().load(request.json)
    
    # Try block checking if email exists already
    try:       
        user = User(
            email = data.get('email'),
            password = bc.generate_password_hash(data['password']).decode('utf8'),
            first_name = data.get('first_name'),
            last_name = data.get('last_name')
        )
        
        # Add user and commit to database
        db.session.add(user)
        db.session.commit()
        
        # Respond to client with the new user with the password excluded 
        return UserSchema(exclude=['password']).dump(user), 201
    
    # Response to client is email is already in use
    except IntegrityError:
        return {'error': 'Email address already in use'}, 409


# Registered User Login
@auth_bp.route('/login/', methods=['POST'])
def auth_login():

    # Checks if user exists
    stmt = db.select(User).filter_by(email= request.json['email'])
    user = db.session.scalar(stmt)

    # If found, checks password and issues access token valid for 1 day
    if user and bc.check_password_hash(user.password, request.json['password']):
        token = create_access_token(identity= str(user.id), expires_delta=timedelta(days=1))
        
        # Response to client with user and token info
        return {'email': user.email, 'token': token, 'is_admin': user.is_admin}
    
    # If not found
    else:
        return {'error': 'Invalid email and password'}, 401


# Create a new admin user (must have admin rights)
@auth_bp.route('/register/admin/', methods=['POST'])
@jwt_required()
def admin_register():
    # Checking if user has admin rights
    authorise()
    
    # Loading requests through schema for validation 
    data = UserSchema().load(request.json)

    # Try block checking if email exists already   
    try:       
        user = User(
            email = data.get('email'),
            password = bc.generate_password_hash(data['password']).decode('utf8'),
            first_name = data.get('first_name'),
            last_name = data.get('last_name'),
            is_admin = True
        )
        
        # Add user and commit to database
        db.session.add(user)
        db.session.commit()
        
        # Respond to client with the new admin with the password excluded 
        return UserSchema(exclude=['password']).dump(user), 201
    
    # Response to client is email is already in use
    except IntegrityError:
        return {'error': 'Email address already in use'}, 409
