from flask import Blueprint, request
from flask_login import current_user, login_required
from app.forms import StashForm
from app.models import db, Stash

stash_routes = Blueprint('stashes', __name__)


def format_errors(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = dict()

    for field in validation_errors:
        errorMessages[field] = [error for error in validation_errors[field]]

    return errorMessages


@stash_routes.route("")
def all_stashes():
    stashes = Stash.query.all()
    return {"stashes": [stash.to_dict_basic() for stash in stashes]}


@stash_routes.route('/<int:id>')
@login_required
def stashes(id):
    '''
    Query for a specific stash by id
    '''
    stash = Stash.query.get(id)
    
    if not stash:
        return {"error": "Stash not Found"}, 404

    return stash.to_dict()


@stash_routes.route('', methods=["POST"])
@login_required
def post_a_stash():
    ''' 
    Post a  new Stash to user profile
    '''

    form = StashForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if form.validate_on_submit():
        new_stash = Stash()
        form.populate_obj(new_stash)
        new_stash.user_id = current_user.id

        db.session.add(new_stash)
        db.session.commit()

        return new_stash.to_dict()

    if form.errors:
        return ({"errors": format_errors(form.errors)}, 400)


@stash_routes.route("/<int:stashId>", methods=["PUT"])
@login_required
def update_stash(stashId):
    '''
    Update a specific stash
    '''
    stash = Stash.query.get(stashId)

    if not stash:
        return {"error": "Stash not Found"}, 404

    form = StashForm()
    form["csrf_token"].data = request.cookies["csrf_token"]

    if stash.user_id != current_user.id:
        return {"errors": "This is not your stash"}, 500

    if form.validate_on_submit():
        form.populate_obj(stash)
        db.session.commit()
        return stash.to_dict()

    if form.errors:
        return {"errors": format_errors(form.errors)}, 400


@stash_routes.route("/<int:stashId>", methods=["DELETE"])
@login_required
def delete_stash(stashId):
    '''
    Delete a stash
    '''
    stash = Stash.query.get(stashId)

    if not stash:
        return {"error": "Stash not Found"}, 404

    if stash.user_id == current_user.id:
        db.session.delete(stash)
        db.session.commit()
        return {"message": "Stash deleted successfully"}, 200
    else:
        return {"errors": "This is not your stash"}, 500




    



