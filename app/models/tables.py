from .db import db, environment, SCHEMA, add_prefix_for_prod

label_image_table = db.Table(
    "label_images",
    db.Column(
        "image_id",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("images.id")),
        primary_key=True,
    ),
    db.Column(
        "label_id",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("labels.id")),
        primary_key=True,
    ),
    schema=SCHEMA if environment == "production" else None,
)

stash_image_table = db.Table(
    "stash_images",
    db.Column(
        "stash_id",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("stashes.id")),
        primary_key=True,
    ),
    db.Column(
        "image_id",
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("images.id")),
        primary_key=True,
    ),
    schema=SCHEMA if environment == "production" else None,
)
