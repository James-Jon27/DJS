from app.models import db, Label, environment, SCHEMA
from sqlalchemy.sql import text

def seed_labels():
    o = Label(
        name = "art"
    )
    t = Label(
        name = "health"
    )
    thr = Label(
        name = "anime"
    )
    fo = Label(
        name = "religion"
    )
    fi = Label(
        name = "science"
    )
    si = Label(
        name= "wallpaper"
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