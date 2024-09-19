from wtforms.validators import DataRequired
from .db import db, environment, SCHEMA

class Image(db.Model):
    __tablename__ = "labels"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)