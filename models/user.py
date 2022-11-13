from init import db, ma 
from marshmallow import fields
from marshmallow.validate import Regexp


# SQLAlchemy model for User resources, tabled called 'users'
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50))
    is_admin = db.Column(db.Boolean, default=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False) 
    # Foreign Key Relationship
    comments = db.relationship('Comment', back_populates='user', cascade='all, delete')
    

# Marshmallow schemas 
class UserSchema(ma.Schema):
    # Validation 
    # First name must have at least 1 character and contain only letters
    first_name = fields.String(required=True, validate=
        Regexp('^(?=\S{1,}$)[a-zA-Z ]+$', error="First names must be at least 1 character long and contain only letters")) 

    # Last name must have at least 1 character and contain only letters
    last_name = fields.String(validate= 
        Regexp('^[a-zA-Z ]+$', error="Last names must be at least 1 character long and contain only letters"))

    # Email address must have at least 6 characters, contain only letters, numbers, @ and . symbols, within the pattern example@example.com 
    email = fields.String(required=True, validate= 
        Regexp('^(?=\S{6,}$)\w+@\w+\.\w+$', error="This does not look like a valid email address"))

    # Password must be between 8 and 20 characters long, include at least 1 uppercase and 1 lowercase letter, a number and a special character
    password = fields.String(required=True, validate= 
        Regexp('^(?=\S{8,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])', 
        error="Users's password must be between 8 and 20 characters long, must include a number and a special character"))


    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'is_admin')
        ordered = True
