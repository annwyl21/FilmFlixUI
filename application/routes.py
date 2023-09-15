from flask import Flask, jsonify, render_template, request
from application import app
import requests
from application.forms import DetailsForm
from application.api_connections import ApiConnect

my_api = ApiConnect()

@app.route('/', methods=['GET', 'POST'])
def index():
	films = my_api.get_films()
	error = ''
	form = DetailsForm()

	if request.method == 'POST':
		film_id = form.film_id.data
		title = form.title.data
		year_released = form.year_released.data
		rating = form.rating.data
		genre = form.genre.data
		duration = form.duration.data
		fieldname = form.fieldname.data
		fieldvalue = form.fieldvalue.data
		id_to_delete = form.id_to_delete.data

		if title and year_released and rating and genre and duration:
			add = {'title': title, 'duration': duration, 'rating': rating, 'genre': genre, 'year_released': year_released}
			confirm = my_api.add_film(add)
			
		elif film_id and fieldname and fieldvalue:
			update = {'film_id': film_id, 'fieldname': fieldname, 'fieldvalue': fieldvalue}
			confirm = my_api.update_film(update)

		elif id_to_delete:
			confirm = my_api.delete_film(id_to_delete)

		else:
			error = 'Required Information Incomplete'
		films = my_api.get_films()
		return render_template('index.html', form=form, films=films, confirmation=confirm)
		 
	return render_template('index.html', form=form, films=films, message=error, confirmation='')
