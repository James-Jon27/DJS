from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LabelForm(FlaskForm):
    name = StringField("Label Name", validators=[DataRequired()])
    submit = SubmitField("Create Label")