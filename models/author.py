from init import db, ma 
from marshmallow import fields  
from marshmallow.validate import Length

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
    first_name = fields.String(required=True, validate=Length(min=1, error="Author's First Name must be at least 1 character"))
    last_name = fields.String(required=True, validate=Length(min=1, error="Author's Last Name must be at least 1 character"))

    class Meta:
        fields = ('id', 'first_name', 'last_name', 'about', 'accolades', 'books')
        ordered = True


