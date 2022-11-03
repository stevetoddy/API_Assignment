from flask import Blueprint, request
from init import db
from models.category import Category, CategorySchema


categories_bp = Blueprint('categories', __name__, url_prefix='/categories')


# Get all categories
@categories_bp.route('/', methods=['GET'])
def all_categories():
    stmt = db.select(Category)
    categories = db.session.scalars(stmt)
    return CategorySchema(many=True).dump(categories)


# Get one category by ID
@categories_bp.route('/<int:id>', methods=['GET'])
def one_category(id):
    stmt = db.select(Category).filter_by(id=id)
    category = db.session.scalar(stmt)
    if category:
        return CategorySchema().dump(category)
    else:
        return {'error': f'No category with id {id}'}, 404


# Get category by Name
@categories_bp.route('/<string:name>/', methods=['GET'])
def category_name(name):
    stmt = db.select(Category).filter_by(name=name)
    category = db.session.scalar(stmt)
    if category:
        return CategorySchema().dump(category)
    else:
        return {'error': f'No category called {name}'}, 404


# Create categories
@categories_bp.route('/', methods=['POST'])
def create_category():
    category = Category(
        name = request.json['name'],
        description = request.json['description']
    )

    db.session.add(category)
    db.session.commit()

    return CategorySchema().dump(category), 201


# Update a category by ID
@categories_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update_category(id):
    stmt = db.select(Category).filter_by(id=id)
    category = db.session.scalar(stmt)
    if category:
        category.name = request.json.get('name') or category.name
        category.description  = request.json.get('description') or category.description

        db.session.commit()
        return CategorySchema().dump(category)
    else:
        return {'error': f'No category with id {id}'}, 404


# Delete a category by ID
@categories_bp.route('/<int:id>', methods=['DELETE'])
def delete_category(id):
    stmt = db.select(Category).filter_by(id=id)
    category = db.session.scalar(stmt)
    if category:
        db.session.delete(category)
        db.session.commit()
        return {'message': f"Category '{category.name}' deleted successfully"}
    else:
        return {'error': f'No category with id {id}'}, 404