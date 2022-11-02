from init import db, ma 


# SQLAlchemy model for Author resources, tabled called 'authors'
class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    accolades = db.Column(db.Text)
    about = db.Column(db.Text)
    

# Marshmallow schemas 
class AuthorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'accolades', 'about')
        ordered = True


