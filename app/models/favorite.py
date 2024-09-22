from sqlalchemy import UniqueConstraint
from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Favorite(db.Model):
    __tablename__ = "favorites"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}


    id = db.Column(db.Integer, primary_key=True, nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("images.id")), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


    #!Relationships
    images = db.relationship("Image", back_populates="favorites")
    users = db.relationship("User",  back_populates="favorites")
   
    def to_dict_basic(self):
        return {
            "id": self.id,
            "image_id": self.image_id,
            "user_id": self.user_id
        }

    def to_dict(self):
        return {
            **self.to_dict_basic(),
            "Users" : [user.to_dict_basic() for user in self.users]
        }
