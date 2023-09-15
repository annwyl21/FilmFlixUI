from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

endpoint = 'https://filmflixrestapi.onrender.com/'

@app.route('/')
def index():
	path = 'api/films'
	url = endpoint + path
	#print(url)

	request = requests.get(url)
	response = request.json()

	film_list = response
	return render_template('index.html', film_list = film_list)

if __name__ == '__main__':
	app.run(debug=True)