from init import db, ma 
from marshmallow import fields


# SQLAlchemy model for Book resources, tabled called 'books'
class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    is_fiction = db.Column(db.Boolean)
    is_kid_friendly = db.Column(db.Boolean)
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
    author = fields.Nested('AuthorSchema', only=['first_name', 'last_name'])
    category = fields.Nested('CategorySchema', only=['name'])
    # Nesting multiple attributes from another table into return
    comments = fields.List(fields.Nested('CommentSchema'))

    class Meta:
        fields = ('id', 'title', 'author', 'category', 'comments', 'is_fiction', 'is_kid_friendly', 'in_store')
        ordered = True


