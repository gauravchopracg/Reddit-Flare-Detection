from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class RedditForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired()])
    submit = SubmitField('Sign In')