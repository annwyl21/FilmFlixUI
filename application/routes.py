from flask import Flask, jsonify, render_template, request
from application import app
import requests
from application.forms import DetailsForm
from application.api_connections import ApiConnect

print('all good')

my_api = ApiConnect()
print('all ok')

@app.route('/', methods=['GET', 'POST'])
def index():
	print('got here')
	films = my_api.get_films()
	error = ''
	form = DetailsForm()

	# endpoint = 'https://filmflixrestapi.onrender.com/'
	# path = 'api/films'
	# url = endpoint + path
	# print(url)
	# request = requests.get(url)
	# response = request.json()
	# films = response

	if request.method == 'POST':
	 	form_id = form.film_id.data
		title = form.title.data
		year_released = form.year_released.data
		rating = form.rating.data
		genre = form.genre.data
		duration = form.duration.data
		print(title)
		error = 'test'
		return render_template('index.html', films=films)
		 
	return render_template('index.html', films=films, message=error)
