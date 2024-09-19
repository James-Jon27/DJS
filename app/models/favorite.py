from .db import db, environment, SCHEMA, add_prefix_for_prod

class Favorite(db.Model):
    __tablename__ = "favorites"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("images.id")), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)

    def to_dict_basic(self):
        return {
            "id": self.id,
            "image_id": self.image_id,
            "user_id": self.user_id
        }

# # Will be in the user.py model soon
# images = db.relationship("Image", secondary=favorites, back_populates="users")

# # Will be in the image.py model soon
# users = db.relationship("User", secondary=favorites, back_populates="images")