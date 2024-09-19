from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from app.api.boto import ALLOWED_EXTENSIONS


class ImageForm(FlaskForm):
    image = FileField(
        "Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))]
    )
    title = StringField("Image Title", validators=[DataRequired(), Length(max=50)])
    description = StringField("Image Description", validators=[Length(max=255)])
    submit = SubmitField("Create Post")
