from .db import db, environment, SCHEMA, add_prefix_for_prod


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
    comment = db.Column(
        db.String(255),
        nullable = False
    )

    user = db.relationship("User", back_populates="comments")

    def to_dict(self):
        return {
            "id": self.id,
            "comment": self.comment,
            "imageId": self.image_id,
            "userId": self.user_id
        }
    
