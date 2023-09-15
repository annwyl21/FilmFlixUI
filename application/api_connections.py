class ApiConnect():
	def __init__(self):
		self.endpoint = 'https://filmflixrestapi.onrender.com/'

	def get_films(self):
		path = 'api/films'
		url = self.endpoint + path

		print(url)

		request = requests.get(url)
		response = request.json()

		films = response
		return films

	def add_film(self):
		pass

	def update_film(self):
		pass

	def delete_film(self):
		pass
