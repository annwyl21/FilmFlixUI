from flask import Flask, jsonify, render_template, request
import requests
from application.form import DetailsForm
from application.api_connections import ApiConnect

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
	films = ApiConnect.get_films()
	#form = DetailsForm()

	# if request.method == 'POST':
	# 	title = form.title.data


	return render_template('index.html', films=films)