from wtforms.validators import DataRequired
from .db import db, environment, SCHEMA, add_prefix_for_prod

class Image(db.Model):
    __tablename__ = "images"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String, nullable=False)
    title = db.Column(db.String(50))
    description = db.Column(db.String(255))

    user = db.relationship("User", back_populates="images")

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
            "User" : self.user.to_dict_basic()
        }