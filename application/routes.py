from flask import Flask, jsonify, render_template, request
from application import app
import requests
#from application.forms import DetailsForm
#from application.api_connections import ApiConnect

print('all good')

#my_api = ApiConnect()
#print('all ok')

@app.route('/')
def index():
	print('got here')
	#films = my_api.get_films()

	endpoint = 'https://filmflixrestapi.onrender.com/'
	path = 'api/films'
	url = endpoint + path
	print(url)
	request = requests.get(url)
	response = request.json()
	films = response

	#form = DetailsForm()

	# if request.method == 'POST':
	# 	title = form.title.data


	return render_template('index.html', films=films)