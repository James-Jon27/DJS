from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import  StringField


class ImageUpdateForm(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    description = StringField("description", validators=[DataRequired()])

