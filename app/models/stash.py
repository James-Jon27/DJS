from .db import db, environment, SCHEMA, add_prefix_for_prod


class Stash(db.Model):
    __tablename__ = "stashes"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=False)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("users.id")),
        nullable=False,
    )
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(150))

    # user = db.relationship("User", back_populates="stash")
    # images = db.relationship("StashImage", back_populates="stash")

    def to_dict(self):
        return {
            "id" : self.id,
            "userId" : self.user_id,
            "name" : self.name,
            "description" : self.description
        }
