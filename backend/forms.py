from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired


class UploadFileForm(FlaskForm):
    file = FileField("Upload File", validators=[InputRequired()])
    submit = SubmitField("Submit")
