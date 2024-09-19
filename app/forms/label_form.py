from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class LabelForm(FlaskForm):
    name = StringField("Label Name", validators=[DataRequired(), Length(max=50)])
    submit = SubmitField("Create Label")