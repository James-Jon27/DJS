from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class StashForm(FlaskForm):
    name = StringField("Stash Name", validators=[DataRequired(), Length(max=30)])
    description = StringField("Stash Description", validators=[Length(max=150)])
    submit = SubmitField("Create Stash")