from init import db, ma 
from marshmallow import fields  
from marshmallow.validate import Regexp


# SQLAlchemy model for Author resources, tabled called 'authors'
class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    accolades = db.Column(db.Text)
    about = db.Column(db.Text)
    # Foreign Key Relationship
    books = db.relationship('Book', back_populates='author')

# Marshmallow schemas 
class AuthorSchema(ma.Schema):
    # Nesting attributes from other tables
    books = fields.List(fields.Nested('BookSchema', only=['title', 'in_store', 'id']))
    
    # Validation 
    
    # First name must have at least 1 character and contain only letters
    first_name = fields.String(required=True, validate=
        Regexp('^(?=\S{1,}$)[a-zA-Z ]+$', error="First names must be at least 1 character long and contain only letters")) 

    # Last name must have at least 1 character and contain only letters
    last_name = fields.String(validate= 
        Regexp('^(?=\S{1,}$)[a-zA-Z ]+$', error="Last names must be at least 1 character long and contain only letters"))


    class Meta:
        fields = ('id', 'first_name', 'last_name', 'about', 'accolades', 'books')
        ordered = True


