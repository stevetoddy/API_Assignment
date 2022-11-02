from init import db, ma 


# SQLAlchemy model for Book resources, tabled called 'books'
class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    is_fiction = db.Column(db.Boolean)
    is_kid_friendly = db.Column(db.Boolean)
    in_store = db.Column(db.Integer)
    

# Marshmallow schemas 
class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'is_fiction', 'is_kid_friendly', 'in_store')
        ordered = True


