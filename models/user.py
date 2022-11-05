from init import db, ma 


# SQLAlchemy model for User resources, tabled called 'users'
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    is_admin = db.Column(db.Boolean, default=False)
    
    # Foreign Key Relationship
    comments = db.relationship('Comment', back_populates='user')
    

# Marshmallow schemas 
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'is_admin')
        ordered = True

