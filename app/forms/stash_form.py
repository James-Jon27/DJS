from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class StashForm(FlaskForm):
    name = StringField("Stash Name", validators=[DataRequired()])
    description = StringField("Stash Description")
    submit = SubmitField("Create Stash")