from flask import Blueprint, request
from init import db
from models.comment import Comment, CommentSchema
from flask_jwt_extended import jwt_required
# COmments Controller Blueprint
comments_bp = Blueprint('comments', __name__, url_prefix='/comments')


# Get all comments (requires authentication)
@comments_bp.route('/', methods=['GET'])
@jwt_required()
def all_comments():
    stmt = db.select(Comment)
    
    # Query to find all comments
    comments = db.session.scalars(stmt)

    # Respond to client with all comments
    return CommentSchema(many=True).dump(comments)


# Get all comments by a User (requires authentication)
@comments_bp.route('/user/<int:user_id>/', methods=['GET'])
@jwt_required()
def all_users_comments(user_id):

    # Query to find all comments by user_id
    stmt = db.select(Comment).filter_by(user_id=user_id)
    comments = db.session.scalars(stmt)

    # Respond to client with all comments by user
    return CommentSchema(many=True).dump(comments)


# Get one comment by ID (requires authentication)
@comments_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def one_comment(id):
    
    # Query to find comment by ID
    stmt = db.select(Comment).filter_by(id=id)
    comment = db.session.scalar(stmt)
    
    # If found
    if comment:

        # Respond to client with comment
        return CommentSchema().dump(comment)

    # If not found
    else:
        return {'error': f'No comment with id {id}'}, 404


# Update a comment by ID (requires authentication)
@comments_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_comment(id):

    # Loading requests through schema for validation 
    data = CommentSchema().load(request.json)

    # Query to find comment by ID
    stmt = db.select(Comment).filter_by(id=id)
    comment = db.session.scalar(stmt)
    
    # If found comment is updated 
    if comment:
        comment.body = data.get('body') or comment.body
        
        # Change committed to database
        db.session.commit()

        # Respond to client with updated comment
        return CommentSchema().dump(comment)
    
    # If not found
    else:
        return {'error': f'No comment with id {id}'}, 404


# Delete a comment by ID (requires authentication)
@comments_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_comment(id):

    # Query to find comment by ID
    stmt = db.select(Comment).filter_by(id=id)
    comment = db.session.scalar(stmt)
    
    # If found
    if comment:

        # Comment deleted and change committed to database
        db.session.delete(comment)
        db.session.commit()

        # Respond to client
        return {'message': f"Comment No.{comment.id} deleted successfully"}
    
    # If not found
    else:
        return {'error': f'No comment with id {id}'}, 404