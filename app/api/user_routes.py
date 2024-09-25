from flask import Blueprint
from flask_login import login_required
from app.models import User, Stash, Favorite, Image


user_routes = Blueprint('users', __name__)


@user_routes.route('/')
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)

    # If user not found
    if not user:
        return {"errors": "User not found"}, 404

    return user.to_dict_basic()


# ! Stashes
@user_routes.route('/<int:id>/stashes')
def user_stashes(id):
    """
    Query for a user by id and returns that users stash
    """
    stashes = Stash.query.filter(Stash.user_id == id).all()
    if not stashes:
        return {"errors": "Stashes not found"}, 404

    return {"Stashes": [stash.to_dict_basic() for stash in stashes]}


#  ! Favorites
@user_routes.route('/<int:id>/favorites')
def user_faves(id):
    """
    Query for a user by id and returns that users stash
    """
    favorites = Favorite.query.filter(Favorite.user_id == id).all()
    if not favorites:
        return {"errors": "Favorites not found"}, 404

    return {"Favorites": [fav.to_dict_basic() for fav in favorites]}


# ! Images
@user_routes.route("/<int:id>/images")
def get_user_images(id):
    """
    Gets all the images posted by the specified user
    """
    images = Image.query.filter(Image.user_id == id).all()
    if not images:
        return {"errors": "Images not found"}, 404

    return {"Images": [image.to_dict_basic() for image in images]}