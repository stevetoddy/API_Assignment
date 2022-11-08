from init import db, ma 
from marshmallow import fields  
from marshmallow.validate import Length

# SQLAlchemy model for Category resources, tabled called 'categories'
class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text) 
    
    # Foreign Key Relationship
    books = db.relationship('Book', back_populates='category')

# Marshmallow schemas 
class CategorySchema(ma.Schema):
    # Validation 
    # Category name must be longer than 1 character
    name = fields.String(required=True, validate=
        Length(min=2, error="Category name must be longer than 1 character"))
    
    # Category description must be longer than 1 character
    name = fields.String(required=True, validate=
        Length(min=2, error="Category description must be longer than 1 character"))

    class Meta:
        fields = ('id', 'name', 'description')
        ordered = True
