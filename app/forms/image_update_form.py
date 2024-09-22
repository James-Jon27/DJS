from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import  StringField


class ImageUpdateForm(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    description = StringField("description", validators=[DataRequired()])
    labels = StringField("Labels", validators=[Length(max=50)])


