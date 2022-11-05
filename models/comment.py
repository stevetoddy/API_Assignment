from init import db, ma 
from marshmallow import fields


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
    user = fields.Nested('UserSchema', only=['id', 'first_name', 'last_name'])
    book = fields.Nested('BookSchema', only=['title', 'author'])

    class Meta:
        fields = ('id', 'body', 'book', 'user' )
        ordered = True
