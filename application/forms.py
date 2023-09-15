from wtforms import IntegerField, SubmitField, StringField
from flask_wtf import FlaskForm

class DetailsForm(FlaskForm):
	film_id = IntegerField('film_id')
	title = StringField('title')
	year_released = IntegerField('year_released')
	rating = StringField('rating')
	genre = StringField('genre')
	duration = IntegerField('duration')

	fieldname = StringField('fieldname')
	fieldvalue = StringField('fieldvalue')

	id_to_delete = IntegerField('id_to_delete')
	
	submit = SubmitField('Submit')