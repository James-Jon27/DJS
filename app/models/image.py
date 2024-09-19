from datetime import datetime
from app.models import label_image, stash_image
from .db import db, environment, SCHEMA, add_prefix_for_prod

class Image(db.Model):
    __tablename__ = "images"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    url = db.Column(db.String, nullable=False)
    title = db.Column(db.String(50))
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    #!Relationships
    user = db.relationship("User", back_populates="images")
    comments = db.relationship("Comment", back_populates="image")
    favorites = db.relationship('Favorite', back_populates="images")

    #!Many to Many
    stashes = db.relationship("StashImage", backref="image", secondary="stash_images")
    labels = db.relationship("LabelImage", back_populates="images", secondary="label_images")

    def to_dict_basic(self):
        return {
            "id": self.id,
            "userId" : self.user_id,
            "url": self.url,
            "title": self.title,
            "description": self.description
        }

    def to_dict(self):
        return {
            **self.to_dict_basic(),
            "User" : self.user.to_dict_basic(),
            "Comments": [comment.to_dict_basic() for comment in self.comments],
            "Favorites": [fav.to_dict_basic() for fav in self.favorites],
            "Labels": [lb.to_dict_basic() for lb in self.labels],
            "Stashes": [stash.to_dict_basic() for stash in self.labels]
        }