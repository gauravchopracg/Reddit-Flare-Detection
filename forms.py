from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class RedditForm(FlaskForm):
    url = StringField('Enter the Reddit URL', validators=[DataRequired()])
    submit = SubmitField('Submit')