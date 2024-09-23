from datetime import datetime
from .tables import label_image_table, stash_image_table
from .db import db, environment, SCHEMA, add_prefix_for_prod


class Image(db.Model):
    __tablename__ = "images"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False
    )
    url = db.Column(db.String, nullable=False)
    title = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # Relationships
    user = db.relationship("User", back_populates="images")
    comments = db.relationship("Comment", back_populates="image", cascade="all, delete")
    favorites = db.relationship(
        "Favorite", back_populates="images", cascade="all, delete"
    )

    # Many-to-Many Relationships
    stashes = db.relationship(
        "Stash", secondary=stash_image_table, back_populates="images", cascade="all, delete"
    )
    labels = db.relationship(
        "Label", secondary=label_image_table, back_populates="images", cascade="all, delete"
    ) 
    
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
            "Stashes": [stash.to_dict_basic() for stash in self.stashes]
        }