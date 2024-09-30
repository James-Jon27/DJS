import app
from app.models import db, Stash, Image, environment, SCHEMA
from app.models.tables import stash_image_table
from sqlalchemy.sql import text

def seed_stash_images():
    stashes = Stash.query.all()
    images = Image.query.all()

    associations = [
        (1, 1),
        (1, 2),
        (2, 3),
        (2, 78),
        (2, 35),
        (2, 43),
        (2, 93),
        (2, 103),
        (2, 87),
        (2, 53),
        (2, 65),
        (2, 39),
        (2, 69),
        (3, 4),
        (3, 5),
        (3, 6),
        (4, 7),
        (4, 8),
        (5, 9),
        (5, 10),
        (5, 11),
    ]

    for stash_id, image_id in associations:
        db.session.execute(
            stash_image_table.insert().values(stash_id=stash_id, image_id=image_id)
        )
    db.session.commit()


def undo_stash_images():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.stash_images RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute(text("DELETE FROM stash_images"))

    db.session.commit()