from flask import Blueprint, request
from app.models import db, Comment
from app.forms import CommentForm
from flask_login import current_user, login_required

comment_routes = Blueprint("comments", __name__)


"""
User can post new comments
"""
@comment_routes.route('/<int:imageId>/new', method=['POST'])
@login_required
def post_new_comment(imageId):
    form = CommentForm()
    form['csrf_token'].data = request.cookies('csrf_token')

    if form.validate_on_submit():
        comment = form.data["comment"]
        new_comment = Comment(
            user_id = current_user.id,
            image_id = imageId,
            comment = comment
        )
        db.session.add(new_comment)
        db.session.commit()
        return new_comment.to_dict_basic()
    
    if form.errors:
        return form.errors
    
    return


"""
User can update their comments
"""
@comment_routes.route('/<int:commentId>', methods=['PUT'])
@login_required
def update_comment(commentId):
    form = CommentForm()
    form['csrf_token'].data = request.cookies('csrf_token')

    if form.validate_on_submit():
        comment = form.data["comment"]
        comment_to_update = Comment.query.get(commentId)
        comment_owner_id = comment_to_update.to_dict_basic()['userId']

        if comment_owner_id == current_user.id:
            comment_to_update.comment = comment
            db.session.commit()
            return comment_to_update.to_dict_basic()
        else:
            return "This is not your comment to update!"
    
    if form.errors:
        return form.errors
    
    return


"""
User can delete their comments
"""
@comment_routes.route('/<int:commentId>', methods=["DELETE"])
@login_required
def delete_comment(commentId):
    comment_to_delete = Comment.query.get(commentId)
    comment_owner_id = comment_to_delete.to_dict_basic()['userId']

    if comment_owner_id == current_user.id:
        db.session.delete(comment_to_delete)
        db.session.commit()
        return f"Comment Id {commentId} has been deleted!"
    else:
        return "This is not your comment to delete!"