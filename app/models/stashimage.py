from .db import db, environment, SCHEMA, add_prefix_for_prod


class StashImage(db.Model):
    __tablename__ = "stashimages"
    __table_args__ = (
        db.UniqueConstraint("stash_id", "image_id", name="unique_stash_image"),
    )

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    stash_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("stashes.id")), nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("images.id")), nullable=False)

    # stash = db.relationship("Stash", back_populates="images", backref="stasheimages")
    # image = db.relationship("Image")

    def to_dict_basic(self):
        return {
            "id": self.id,
            "stash_id": self.stash_id,
            "image_id": self.image_id,
        }

    def to_dict(self):
        return {
            **self.to_dict_basic(),
            "Stash" : self.stash.to_dict_basic(),
        }