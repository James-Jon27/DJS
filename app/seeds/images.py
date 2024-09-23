from app.models import db, Image, environment, SCHEMA
from sqlalchemy.sql import text

def seed_images():
    on = Image(
        user_id=1,
        url="https://upload.wikimedia.org/wikipedia/commons/d/d9/Opening_chess_position_from_black_side.jpg",
        title="Black Side"
    )
    tw = Image(
        user_id=1,
        url="https://upload.wikimedia.org/wikipedia/commons/f/f1/Chess_piece_-_Black_king.JPG",
        title="Black King"
    )
    th = Image(
        user_id=1,
        url="https://www.tvqc.com/wp-content/uploads/2019/03/That-Time-I-Got-Reincarnated-as-a-Slime.jpg",
        title="Reincarnated as a Slime",
        description="This is NOT a good anime!"
    )
    fo = Image(
        user_id=2,
        url="https://assets.epicurious.com/photos/58d3fed8e2c8295cfbf4a52f/master/pass/ginger_root_pile_23032017.jpg",
        title="How to cook with Ginger",
        description="I know a few good recipes for ginger, please reach out to me if you want to get started!!!"
    )
    fi = Image(
        user_id=2,
        url="https://cdn.shopify.com/s/files/1/0940/8252/files/Ginger_Root-01_1024x1024.jpg?v=1538426708",
        title="Ginger",
        description="Nuff Said"
    )
    si = Image(
        user_id=2, 
        url="https://a-z-animals.com/media/2022/10/iStock-1253070568.jpg",
        title="New Batch"
    )
    se = Image(
        user_id=2, 
        url="https://www.oxygen.ie/wp-content/uploads/2018/05/ginger.jpg",
        title="Beautiful Ginger King",
        description="We are ginger and we are proud!"
    )
    ei = Image(
        user_id=2,
        url="http://topgingers.weebly.com/uploads/1/9/7/7/19776369/8794572.jpeg",
        title="Ron Weasly"
    )
    ni = Image(
        user_id=3,
        url="https://www.goodcore.co.uk/blog/wp-content/uploads/2019/08/coding-vs-programming-2.jpg",
        title="Ill Never Find a Job"
    )
    te = Image(
        user_id=3,
        url="https://cdn.static-economist.com/sites/default/files/images/2015/09/blogs/economist-explains/code2.png",
        title="Tracking Tweets"
    )
    el = Image(
        user_id=3,
        url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/2d78d141-1f64-44c8-976b-7321284e5147/dfjfdbh-02721342-e03d-4748-965f-f5fd5773baba.png",
        title="Literally so me..."
    )

    lst = [on, tw, th, fo, fi, si, se, ei, ni, te, el]
    for image in lst:
        db.session.add(image)

    db.session.commit()

def undo_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM images"))
        
    db.session.commit()