from init import db, ma 


# SQLAlchemy model for Comment resources, tabled called 'comments'
class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    

# Marshmallow schemas 
class CommentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'body')
        ordered = True
