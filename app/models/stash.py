from .tables import stash_image_table
from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Stash(db.Model):
    __tablename__ = "stashes"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False
    )
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(150), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    user = db.relationship("User", back_populates="stashes")
    images = db.relationship(
        "Image", secondary=stash_image_table, back_populates="stashes"
    )

    def to_dict_basic(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "name": self.name,
            "description": self.description,
            "updatedAt": self.updated_at,
        }

    def to_dict(self):
        return {
            **self.to_dict_basic(),
            "User" : self.user.to_dict_basic(),
            "Images": [img.to_dict() for img in self.images]
        }
