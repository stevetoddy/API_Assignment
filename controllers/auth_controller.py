from flask import Blueprint, request, abort
from init import db, bc, jwt
from models.user import User, UserSchema
from sqlalchemy.exc import IntegrityError
from datetime import timedelta
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


# Admin Authorisation function
def authorise():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if not user.is_admin:
        abort(401)


# Create a new user
@auth_bp.route('/register/', methods=['POST'])
@jwt_required()
def auth_register():
    try:       
        user = User(
            email = request.json['email'],
            password = bc.generate_password_hash(request.json['password']).decode('utf8'),
            first_name = request.json.get('first_name'),
            last_name = request.json.get('last_name')
        )
        
        db.session.add(user)
        db.session.commit()
        
        # Respond to client with the UserSchema with the password excluded 
        return UserSchema(exclude=['password']).dump(user), 201
    
    except IntegrityError:
        return {'error': 'Email address already in use'}, 409


# Registered User Login
@auth_bp.route('/login/', methods=['POST'])
def auth_login():
    # Checks if user exists
    stmt = db.select(User).filter_by(email= request.json['email'])
    user = db.session.scalar(stmt)
    # If a user is found, checks password and issues access token valid for 1 day
    if user and bc.check_password_hash(user.password, request.json['password']):
        token = create_access_token(identity= str(user.id), expires_delta=timedelta(days=1))
        return {'email': user.email, 'token': token, 'is_admin': user.is_admin}
    else:
        return {'error': 'Invalid email and password'}, 401


# Create a new admin user (must have admin rights)
@auth_bp.route('/register/admin/', methods=['POST'])
@jwt_required()
def admin_register():
    if not authorise():
        return {"error": "Only an admin user can create an admin user"}
    try:       
        user = User(
            email = request.json['email'],
            password = bc.generate_password_hash(request.json['password']).decode('utf8'),
            first_name = request.json.get('first_name'),
            last_name = request.json.get('last_name'),
            is_admin = True
        )
        
        db.session.add(user)
        db.session.commit()
        
        # Respond to client with the UserSchema with the password excluded 
        return UserSchema(exclude=['password']).dump(user), 201
    
    except IntegrityError:
        return {'error': 'Email address already in use'}, 409
