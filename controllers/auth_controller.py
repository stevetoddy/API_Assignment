from flask import Blueprint, request
from init import db, bc, jwt
from models.user import User, UserSchema
from sqlalchemy.exc import IntegrityError
from datetime import timedelta
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Create a new user
@auth_bp.route('/register/', methods=['POST'])
@jwt_required
def auth_register():
    try:       
        # Create a new User
        user = User(
            email = request.json['email'],
            password = bc.generate_password_hash(request.json['password']).decode('utf8'),
            first_name = request.json.get('first_name'),
            last_name = request.json.get('last_name')
        )
        
        # Add and commit user to DB
        db.session.add(user)
        db.session.commit()
        
        # Respond to client with the UserSchema and the password excluded 
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

# def authorise():
#     user_id = get_jwt_identity()
#     stmt = db.select(User).filter_by(id=user_id)
#     user = db.session.scalar(stmt)
    

# @auth_bp.route('/users/', methods=['GET'])
# # @jwt_required()
# def get_all_users():

#     # if not authorise():
#     #     return {'error': 'You must be admin'}, 401


#     stmt = db.select(User)
#     users = db.session.scalars(stmt)
#     return UserSchema(many=True, exclude=['password']).dump(users)