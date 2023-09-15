from wtforms import IntegerField, SubmitField, StringField
from flask_wtf import FlaskForm

class DetailsForm(FlaskForm):
	title = StringField('title')