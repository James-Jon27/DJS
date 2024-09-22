from flask import Blueprint
from flask_login import current_user, login_required
from app.models import db, Favorite

favorite_routes = Blueprint("favorites", __name__)

@favorite_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def del_fav(id):
    fav = Favorite.query.get(id)

    if fav.user_id == current_user.id:
        db.session.delete(fav)
        db.session.commit()
        return {"message": "Successfully deleted"}
    else:
        return {"errors": "This is not your favorite"}, 500