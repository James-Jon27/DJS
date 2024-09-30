from app.models import db, Label, Image, environment, SCHEMA
from app.models.tables import label_image_table
from sqlalchemy.sql import text


def seed_label_images():
    labels = Label.query.all()  # art, health, anime, religion, science, wallpaper
    images = Image.query.all()

    associations = [
        (1, 1),
        (1, 45),
        (1, 56),
        (1, 11),
        (1, 72),
        (1, 71),
        (1, 32),
        (1, 50),
        (1, 90),
        (1, 104),
        (1, 69),
        (1, 23),
        (2, 4),
        (2, 5),
        (2, 6),
        (2, 34),
        (2, 57),
        (2, 43),
        (2, 48),
        (2, 94),
        (2, 74),
        (2, 40),
        (2, 41),
        (3, 3),
        (4, 7),
        (4, 8),
        (4, 57),
        (4, 79),
        (4, 74),
        (4, 27),
        (4, 97),
        (4, 107),
        (4, 43),
        (4, 76),
        (4, 69),
        (4, 30),
        (4, 3),
        (4, 5),
        (4, 9),
        (5, 4),
        (5, 5),
        (5, 6),
        (5, 69),
        (5, 76),
        (5, 46),
        (5, 60),
        (5, 61),
        (5, 16),
        (5, 107),
        (5, 97),
        (5, 55),
        (5, 66),
        (5, 100),
        (5, 29),
        (5, 52),
        (5, 89),
        (5, 7),
        (6, 85),
        (6, 48),
        (6, 67),
        (6, 93),
        (6, 75),
        (6, 36),
        (6, 90),
        (6, 55),
        (6, 44),
        (6, 39),
        (6, 100),
        (6, 71),
        (6, 60),
        (6, 46),
        (6, 57),
        (6, 72),
        (6, 68),
        (6, 82),
        (6, 38),
        (6, 92),
        (6, 41),
        (6, 65),
        (6, 80),
        (6, 47),
        (6, 34),
        (6, 99),
        (6, 42),
        (6, 64),
        (6, 70),
        (6, 88),
        (6, 52),
        (6, 59),
        (6, 86),
        (6, 69),
        (6, 73),
        (6, 61),
        (6, 54),
        (6, 37),
        (6, 95),
        (6, 83),
        (6, 50),
        (6, 97),
        (6, 45),
        (6, 49),
        (6, 91),
        (6, 84),
        (6, 78),
        (6, 40),
        (6, 63),
        (6, 76),
    ]

    for label_id, image_id in associations:
        db.session.execute(
            label_image_table.insert().values(label_id=label_id, image_id=image_id)
        )
    db.session.commit()


def undo_label_images():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.label_images RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute(text("DELETE FROM label_images"))

    db.session.commit()
