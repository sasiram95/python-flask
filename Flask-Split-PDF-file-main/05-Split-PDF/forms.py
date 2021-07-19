from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField


class PDFForm(FlaskForm):
    PDF = FileField('Select PDF File', validators=[FileRequired(),FileAllowed(['pdf', 'PDF'])])
    submit = SubmitField('Update')
    
