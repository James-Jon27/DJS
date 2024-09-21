from flask import Blueprint
from flask_login import login_required
from app.models import User, Stash, Favorite


user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    return user.to_dict()


@user_routes.route('/<int:id>/stashes')
@login_required
def user_stashes(id):
    """
    Query for a user by id and returns that users stash
    """
    stashes = Stash.query.filter(Stash.user_id == id).all()
    return {"stashes": [stash.to_dict_basic() for stash in stashes]}


@user_routes.route('/<int:id>/favorites')
@login_required
def user_faves(id):
    """
    Query for a user by id and returns that users stash
    """
    favorites = Favorite.query.filter(Favorite.user_id == id).all()
    return {"favorites": [fav.to_dict_basic() for fav in favorites]}