from init import db, ma 
from marshmallow import fields
from marshmallow.validate import Length


# SQLAlchemy model for Comment resources, tabled called 'comments'
class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    # Foreign Key Relationship
    user = db.relationship('User', back_populates='comments')
    book = db.relationship('Book', back_populates='comments')


# Marshmallow schemas 
class CommentSchema(ma.Schema):
    # Nesting attributes from other tables into return
    user = fields.Nested('UserSchema', only=['id', 'first_name', 'last_name'])
    book = fields.Nested('BookSchema', only=['id', 'title', 'author'])
    
    # Validation 
    # Comment body name must be longer than 1 character
    body = fields.String(required=True, validate=
        Length(min=2, error="Comment must be longer than 1 character"))


    class Meta:
        fields = ('id', 'body', 'book', 'user' )
        ordered = True
