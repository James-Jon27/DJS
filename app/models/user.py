from datetime import datetime
from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50))
    hashed_password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    #!Relationships
    comments = db.relationship("Comment", back_populates="user")
    stashes = db.relationship("Stash", back_populates="user")
    images = db.relationship("Image", back_populates="user")
    favorites = db.relationship("Favorite", back_populates="users")

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict_basic(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'firstName' : self.first_name,
            "lastName" : self.last_name
        }

    def to_dict(self):
        return {
            **self.to_dict_basic(),
            "Images": [image.to_dict_basic() for image in self.images],
            "Comments": [comment.to_dict_basic() for comment in self.comments],
            "Stashes" : [stash.to_dict_basic() for stash in self.stashes],
            "Favorites": [fav.to_dict_basic() for fav in self.favorites]
        }
