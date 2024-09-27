from flask import Blueprint, request
from app.models import db, Comment
from app.forms import CommentForm
from flask_login import current_user, login_required

comment_routes = Blueprint("comments", __name__)

def format_errors(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = dict()

    for field in validation_errors:
        errorMessages[field] = [error for error in validation_errors[field]]

    return errorMessages


@comment_routes.route('')
def get_all_comments():
    """
    Get all comments
    """
    all_comments = Comment.query.all()
    return {'comments': [comment.to_dict_basic() for comment in all_comments]}
    # return "This is a return from get all comments!"


@comment_routes.route('/<int:id>', methods=['PUT'])
@login_required
def update_comment(id):
    """
    User can update their comments
    """
    form = CommentForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    comment_to_update = Comment.query.get(id)

    #! If comment does not exist
    if not comment_to_update:
        return {"errors": "Comment not Found"}, 404

    #! If curr user does not own comment
    if comment_to_update.user_id != current_user.id:
        return {"errors": "This is not your comment to update!"}, 500

    #! Use information from form to update 
    if form.validate_on_submit():
        comment = form.data["comment"]
        comment_to_update.comment = comment
        db.session.commit()
        return comment_to_update.to_dict()
    
    if form.errors:
        return {"errors": format_errors(form.errors)}


@comment_routes.route('/<int:id>', methods=["DELETE"])
@login_required
def delete_comment(id):
    """
    User can delete their comments
    """
    comment_to_delete = Comment.query.get(id)

    #! If comment does not exist
    if not comment_to_delete:
        return {"errors": "Comment not found"}, 404
    
    #! If curr user does not own comment
    if comment_to_delete.user_id != current_user.id:
        return {"errors": "This is not your comment to delete!"}, 403

    db.session.delete(comment_to_delete)
    db.session.commit()
    
    return {"message":"Comment has been deleted!"}