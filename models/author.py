from init import db, ma 
from marshmallow import fields


# SQLAlchemy model for Author resources, tabled called 'authors'
class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    accolades = db.Column(db.Text)
    about = db.Column(db.Text)
    # Foreign Key Relationship
    books = db.relationship('Book', back_populates='author')

# Marshmallow schemas 
class AuthorSchema(ma.Schema):
    books = fields.Nested('BookSchema')

    class Meta:
        fields = ('id', 'first_name', 'last_name', 'about', 'accolades')
        ordered = True


