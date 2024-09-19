from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash


class Comments(db.Model):
    __tablename__ = "comments"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("users.id")),
        nullable=False,
    )
    image_id = db.Column(
        db.Integer, db.ForeignKey(add_prefix_for_prod("images.id")), nullable=False
    )
    
