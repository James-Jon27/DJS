from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, ValidationError
from wtforms import  StringField


def validate_labels(form, field):
        labels = field.data
        labels = labels.strip()
        if(labels.endswith(',')):
                labels = labels[:-1]
        labels = labels.split(',')
        for i, label in enumerate(labels):
            labels[i] = label.strip()

        for label in labels:
            if(len(label) > 20):
                raise ValidationError('Each label must be less than 20 characters')


class ImageUpdateForm(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    description = StringField("description")
    labels = StringField("Labels", validators=[validate_labels])
    



