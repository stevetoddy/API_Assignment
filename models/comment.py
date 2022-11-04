from init import db, ma 


# SQLAlchemy model for Comment resources, tabled called 'comments'
class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    users = db.relationship('User', back_populates='comments')
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    books = db.relationship('Book', back_populates='comments')

    

# Marshmallow schemas 
class CommentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'body')
        ordered = True
