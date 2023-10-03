import requests
from flask import Flask, jsonify, render_template, request


class ApiConnect():
	def __init__(self):
		self.endpoint = 'https://filmflixrestapi.onrender.com/'
		#self.endpoint = 'http://localhost:5000/'

	def get_films(self):
		path = 'api/films'
		url = self.endpoint + path

		request = requests.get(url)
		response = request.json()

		films = response
		return films
	
	def get_tail(self):
		path = 'api/films'
		url = self.endpoint + path

		request = requests.get(url)
		response = request.json()

		films = response
		tail = films[-5:]
		return tail
	
	def populate_field_selection(self):
		path = 'api/populate'
		url = self.endpoint + path

		request = requests.get(url)
		response = request.json()

		selections = response
		return selections
	
	def check_film(self, word):
		path = 'api/check'
		url = self.endpoint + path

		headers = {
			'Content-type': 'application/json'
		}

		request = requests.post(url, headers=headers, json=word)
		response = request.json()

		confirmation = response
		return confirmation

	def add_film(self, add_dict):
		path = 'api/add'
		url = self.endpoint + path

		headers = {
			'Content-type': 'application/json'
		}

		request = requests.post(url, headers=headers, json=add_dict)
		response = request.json()

		confirmation = response
		return confirmation

	def update_film(self, update_dict):
		path = 'api/amend'
		url = self.endpoint + path

		headers = {
			'Content-type': 'application/json'
		}

		request = requests.patch(url, headers=headers, json=update_dict)
		response = request.json()

		confirmation = response
		return confirmation

	def delete_film(self, id_to_delete):
		path = 'api/remove/'
		url = self.endpoint + path + str(id_to_delete)

		request = requests.delete(url)
		response = request.json()

		confirmation = response
		return confirmation
