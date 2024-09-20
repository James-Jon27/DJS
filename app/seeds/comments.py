from app.models import db, Comment, environment, SCHEMA
from sqlalchemy.sql import text

def seed_comments():
    on = Comment(
        user_id=1,
        image_id=6,
        comment="I think ginger is a wonderful root!"
    )
    tw = Comment(
        user_id=1,
        image_id=7,
        comment="No soul (My apologies to any future ginger employer)"
    ) 
    th = Comment(
        user_id=1,
        image_id=4,
        comment="What's your email, I'd love a few recipes"
    ) 
    fo = Comment(
        user_id=1,
        image_id=11,
        comment="I wonder if coding is fun, I should pick it up"
    ) 
    fi = Comment(
        user_id=2,
        image_id=10,
        comment="I don't think your title accurately describes what this code block does"
    ) 
    si = Comment(
        user_id=2,
        image_id=11,
        comment="You forgot how much i pull out my hair :P"
    ) 
    se = Comment(
        user_id=2,
        image_id=2,
        comment="THEEE ROOOOOOOOOOKKKKKK"
    ) 
    ei = Comment(
        user_id=3,
        image_id=2,
        comment="THEEEE ROOOOOOOOKKKKKKK"
    ) 
    ni = Comment(
        user_id=3,
        image_id=1,
        comment="He sac'd the queen!"
    ) 
    te = Comment(
        user_id=3,
        image_id=5,
        comment="I din't know ginger had so many benefits"
    ) 

    lst = [on, tw, th, fo, fi, si, se, ei, ni, te]
    for com in lst:
        db.session.add(com)
    db.session.commit()

def undo_comments():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.comments RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM comments"))
        
    db.session.commit()
