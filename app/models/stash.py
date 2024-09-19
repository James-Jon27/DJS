from app.models import stash_image
from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Stash(db.Model):
    __tablename__ = "stashes"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("users.id")),
        nullable=False,
    )
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(150))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    user = db.relationship("User", back_populates="stashes")
    images = db.relationship("StashImage", backref="stash", secondary="stash_images")

    def to_dict(self):
        return {
            "id" : self.id,
            "userId" : self.user_id,
            "name" : self.name,
            "description" : self.description
        }
