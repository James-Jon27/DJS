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
    user_holder = {}
    for user in users:
        user_holder[user.id] = user.to_dict_basic()
    return user_holder


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
        return {"errors": "Stashes not found"}

    stash_holder = {}
    for stash in stashes:
        stash_holder[stash.id] = stash.to_dict_basic()
    return stash_holder


#  ! Favorites
@user_routes.route('/<int:id>/favorites')
def user_faves(id):
    """
    Query for a user by id and returns that users stash
    """
    favorites = Favorite.query.filter(Favorite.user_id == id).all()
    if not favorites:
        return {"errors": "Favorites not found"}, 404
    fav_holder = {}
    for favorite in favorites:
        fav_holder[favorite.id] = favorite.to_dict_basic()
    return fav_holder


# ! Images
@user_routes.route("/<int:id>/images")
def get_user_images(id):
    """
    Gets all the images posted by the specified user
    """
    images = Image.query.filter(Image.user_id == id).all()
    if not images:
        return {"errors": "Images not found"}, 404

    image_holder = {}
    for image in images:
        image_holder[image.id] = image.to_dict()
    return image_holder