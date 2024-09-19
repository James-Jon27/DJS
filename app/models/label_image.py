from .db import db, environment, SCHEMA, add_prefix_for_prod

class LabelImage(db.Model):
    __tablename__ = "label_images"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("images.id")), nullable=False)
    label_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("labels.id")), nullable=False)

    def to_dict_basic(self):
        return {
            "id": self.id,
            "image_id": self.image_id,
            "label_id": self.label_id
        }

# # Will be in the image.py model soon
# labels = db.relationship("Label", secondary=label_images, back_populates="images")

# # Will be in the labels.py model soon
# images = db.relationship("Image", secondary=label_images, back_populates="labels")