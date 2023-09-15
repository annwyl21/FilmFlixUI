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
		form_id = form.film_id.data
		title = form.title.data
		year_released = form.year_released.data
		rating = form.rating.data
		genre = form.genre.data
		duration = form.duration.data
		print(title)
		error = 'test'
		return render_template('results.html', films=films)
		 
	return render_template('index.html', films=films, message=error)
