from flask import Blueprint
from flask_login import current_user, login_required
from app.models import db, Favorite, Image

favorite_routes = Blueprint("favorites", __name__)

@favorite_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def del_fav(id):
    fav_to_delete = Favorite.query.get(id)


    if not fav_to_delete:
        return {"errors": "This image is not a favorite"}, 404    #! If curr user owns favorite
    if fav_to_delete.user_id == current_user.id:
        img = Image.query.get(fav_to_delete.image_id)
        db.session.delete(fav_to_delete)
        db.session.commit()
        return img.to_dict()
    else:
        return {"errors": "This is not your favorite"}, 500