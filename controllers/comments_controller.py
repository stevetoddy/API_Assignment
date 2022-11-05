from flask import Blueprint, request
from init import db
from models.comment import Comment, CommentSchema
from flask_jwt_extended import jwt_required, get_jwt_identity


comments_bp = Blueprint('comments', __name__, url_prefix='/comments')


# Get all comments (requires authentication)
@comments_bp.route('/', methods=['GET'])
@jwt_required()
def all_comments():
    stmt = db.select(Comment)
    comments = db.session.scalars(stmt)
    return CommentSchema(many=True).dump(comments)

# Get all comments by a User (requires authentication)
@comments_bp.route('/user/<int:user_id>/', methods=['GET'])
@jwt_required()
def all_users_comments(user_id):
    stmt = db.select(Comment).filter_by(user_id=user_id)
    comments = db.session.scalars(stmt)
    return CommentSchema(many=True).dump(comments)


# Get one comment by ID (requires authentication)
@comments_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def one_comment(id):
    stmt = db.select(Comment).filter_by(id=id)
    comment = db.session.scalar(stmt)
    if comment:
        return CommentSchema().dump(comment)
    else:
        return {'error': f'No comment with id {id}'}, 404


# Update a comment by ID (requires authentication)
@comments_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_comment(id):
    stmt = db.select(Comment).filter_by(id=id)
    comment = db.session.scalar(stmt)
    if comment:
        comment.body = request.json.get('body') or comment.body

        db.session.commit()
        return CommentSchema().dump(comment)
    else:
        return {'error': f'No comment with id {id}'}, 404


# Delete a comment by ID (requires authentication)
@comments_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_comment(id):
    stmt = db.select(Comment).filter_by(id=id)
    comment = db.session.scalar(stmt)
    if comment:
        db.session.delete(comment)
        db.session.commit()
        return {'message': f"Comment No.{comment.id} deleted successfully"}
    else:
        return {'error': f'No comment with id {id}'}, 404