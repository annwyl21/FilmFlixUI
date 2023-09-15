from wtforms import IntegerField, SubmitField, StringField
from flask_wtf import FlaskForm

class DetailsForm(FlaskForm):
	film_id = IntegerField('film_id')
	title = StringField('title')
	year_released = IntegerField('year_released')
	rating = StringField('rating')
	genre = StringField('genre')
	duration = IntegerField('duration')
	
	submit = SubmitField('Submit')