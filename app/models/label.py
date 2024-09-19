from app.models import label_image
from .db import db, environment, SCHEMA

class Label(db.Model):
    __tablename__ = "labels"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False, unique=True)

    images = db.relationship('LabelImage', back_populates="labels", secondary="label_image")

    def to_dict_basic(self):
        return {
            "id": self.id,
            "name": self.name
        }
    
    def to_dict(self):
        return {
            **self.to_dict_basic(),
            "Images": [i.to_dict_basic() for i in self.images]
        }