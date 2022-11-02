from init import db, ma 


# SQLAlchemy model for Category resources, tabled called 'categories'
class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    

# Marshmallow schemas 
class CategorySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description')
        ordered = True
