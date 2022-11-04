from flask import Blueprint, request
from init import db, bc
from models.user import User, UserSchema
from sqlalchemy.exc import IntegrityError

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register/', methods=['POST'])
def auth_register():
    try:       
        # Create a new User
        user = User(
            email = request.json['email'],
            password = bcrypt.generate_password_hash(request.json['password']).decode('utf8'),
            name = request.json.get('name')
        )
        
        # Add and commit user to DB
        db.session.add(user)
        db.session.commit()
        
        #Respond to client [excluded info from being sent back]
        return UserSchema(exclude=['password']).dump(user), 201
    
    except IntegrityError:
        return {'error': 'Email address already in use'}, 409
