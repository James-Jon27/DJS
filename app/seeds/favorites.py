from app.models import db, Favorite, environment, SCHEMA
from sqlalchemy.sql import text


def seed_favorites():
    users = [1, 2, 3, 4, 5, 6, 7]
    images = [1, 2, 4, 5, 9, 10, 11, 29, 52, 89, 100, 107, 42, 56]
    img1 = [3, 17, 19, 25, 26, 27, 83, 95, 47, 57]
    img2 = [3, 13, 19, 22, 27, 55, 43, 69, 102, 95]
    img3 = [3, 12, 22, 25, 37, 39, 43, 105, 87]
    img5 = [3, 12, 25, 42, 80, 69, 83]
    img7 = [17, 25, 83, 69, 102, 37, 12, 83]
    favorites = []

    for user_id in users:
        for image_id in images:
            favorites.append(Favorite(image_id=image_id, user_id=user_id))

    for image_id in img1:
        favorites.append(Favorite(image_id=image_id, user_id=1))

    for image_id in img2:
        favorites.append(Favorite(image_id=image_id, user_id=2))

    for image_id in img3:
        favorites.append(Favorite(image_id=image_id, user_id=3))

    for image_id in img5:
        favorites.append(Favorite(image_id=image_id, user_id=5))

    for image_id in img7:
        favorites.append(Favorite(image_id=image_id, user_id=7))

    for favorite in favorites:
        db.session.add(favorite)

    db.session.commit()


def undo_favorites():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.favorites RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute(text("DELETE FROM favorites"))

    db.session.commit()
