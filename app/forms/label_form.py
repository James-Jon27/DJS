from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length

class LabelForm(FlaskForm):
    name = StringField("Label Name", validators=[Length(max=50)])
    submit = SubmitField("Create Label")