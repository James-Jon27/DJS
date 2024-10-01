from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, Length, ValidationError
from wtforms import  StringField
from app.api.s3_helper import ALLOWED_EXTENSIONS

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
                raise ValidationError('Each label must be at most 20 characters!')

class ImageForm(FlaskForm):
    image = FileField("Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
    title = StringField("title", validators=[DataRequired()])
    description = StringField("description")
    labels = StringField("Labels", validators=[validate_labels])
    
