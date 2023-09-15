from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

endpoint = 'https://filmflixrestapi.onrender.com/'

@app.route('/')
def index():
	path = 'api/films'
	url = endpoint + path

	request = requests.get(url)
	response = request.json()

	films = response
	return render_template('index.html', films=films)

if __name__ == '__main__':
	app.run(debug=True)