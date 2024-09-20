from app.models import db, Label, environment, SCHEMA
from sqlalchemy.sql import text

def seed_labels():
    o = Label(
        name = "Art"
    )
    t = Label(
        name = "Health"
    )
    thr = Label(
        name = "Anime"
    )
    fo = Label(
        name ="Religion"
    )
    fi = Label(
        name = "Science"
    )
    si = Label(
        name="Wallpaper"
    )

    lst = [o, t, thr, fo, fi, si]
    for label in lst:
        db.session.add(label)

    db.session.commit()

def undo_labels():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.labels RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM labels"))
        
    db.session.commit()