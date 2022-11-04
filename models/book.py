from init import db, ma 


# SQLAlchemy model for Book resources, tabled called 'books'
class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    is_fiction = db.Column(db.Boolean)
    is_kid_friendly = db.Column(db.Boolean)
    in_store = db.Column(db.Integer)
    #Foreign Keys
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    author = db.relationship('Author', back_populates='books')
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)    
    categories = db.relationship('Category', back_populates='books')
    # Foreign Key Relationship
    comments = db.relationship('Comment', back_populates='books', cascade='all, delete')
    

# Marshmallow schemas 
class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'author_id', 'category_id', 'is_fiction', 'is_kid_friendly', 'in_store')
        ordered = True


