from .db import db, environment, SCHEMA

class Label(db.Model):
    __tablename__ = "labels"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False, unique=True)