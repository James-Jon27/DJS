from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Comment(db.Model):
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
    comment = db.Column(
        db.String(255),
        nullable = False
    )
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    user = db.relationship("User", back_populates="comments")
    image = db.relationship("Image", back_populates="comments")

    def to_dict_basic(self):
        return {
            "id": self.id,
            "comment": self.comment,
            "imageId": self.image_id,
            "userId": self.user_id,
            "updatedAt": self.updated_at
        }
    
    def to_dict(self):
        return {
            **self.to_dict_basic(),
            "User" : self.user.to_dict_basic(),
        }
