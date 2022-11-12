from init import db, ma 
from marshmallow import fields
from marshmallow.validate import Length, Regexp

# SQLAlchemy model for Book resources, tabled called 'books'
class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    is_fiction = db.Column(db.Boolean)
    in_store = db.Column(db.Integer)
    # Foreign Keys
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)    
    # Foreign Key Relationship
    author = db.relationship('Author', back_populates='books')    
    category = db.relationship('Category', back_populates='books')
    comments = db.relationship('Comment', back_populates='book', cascade='all, delete')
    

# Marshmallow schemas 
class BookSchema(ma.Schema):
    # Nesting attributes from other tables into return
    author = fields.Nested('AuthorSchema', only=['id', 'first_name', 'last_name'])
    category = fields.Nested('CategorySchema', only=['id', 'name'])
    
    # Nesting multiple attributes from linked table into return
    comments = fields.List(fields.Nested('CommentSchema', only=['id', 'body', 'user']))

    # Validation 
    # Titles must have at least 1 character
    title = fields.String(required=True, validate=
        Length(min=1, error="Title must be at least 1 character long"))
    # Is Fiction only accepts boolean values, True (true, 1) or False (false, 0)
    is_fiction = fields.Boolean(required=True)
    # In Store must be an integer
    in_store = fields.Integer(required=True) 
    # Author ID must be an integer
    author_id = fields.Integer(required=True) 
    # Category ID must be an integer
    category_id = fields.Integer(required=True) 

    class Meta:
        fields = ('id', 'title', 'author_id', 'author', 'category_id', 'category', 'is_fiction', 'in_store', 'comments')
        ordered = True


