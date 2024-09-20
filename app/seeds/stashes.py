from app.models import db, Stash, environment, SCHEMA
from sqlalchemy.sql import text


def seed_stashes():
    one = Stash(
        user_id = 1,
        name = "Chess",
        description="Magnus Carlsen",
    )

    two = Stash(
        user_id=1,
        name="Reincarnation",
        description="Slimes and Buddhas",
    )

    three = Stash(
        user_id=2,
        name="Ginger",
        description="IS NOT REDHEADS",
    )

    four = Stash(
        user_id=2,
        name="Ginger",
        description="IS REDHEADS",
    )
    
    five = Stash(
        user_id = 3,
        name = "Hello World",
        description="I was not done properly",
    )
    
    lst = [one, two, three, four, five]

    for stash in lst:
        db.session.add(stash)

    db.session.commit()

def undo_stashes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.stashes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM stashes"))
        
    db.session.commit()