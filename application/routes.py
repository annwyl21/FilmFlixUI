from flask import Flask, jsonify, render_template, request
from application import app
import requests
from application.forms import DetailsForm
from application.api_connections import ApiConnect
import datetime

my_api = ApiConnect()
today = datetime.date.today()
year = today.year

@app.route('/', methods=['GET', 'POST'])
def index():
	films = my_api.get_tail()
	error = ''
	form = DetailsForm()

	if request.method == 'POST':
		word_to_lookup = form.word_to_lookup.data

		if word_to_lookup:
			if word_to_lookup.isalnum():
				check = {'word': word_to_lookup}
				search_results = my_api.check_film(check)
			else:
				error = "Data Entry Error"
				search_results = ''
		
		else:
			error = 'Required Information Incomplete'
			search_results = ''
		films = my_api.get_tail()
		return render_template('index.html', form=form, films=films, search_results=search_results, message=error)
		 
	return render_template('index.html', form=form, films=films, message=error, confirmation='')

@app.route('/admin/<action>', methods=['GET', 'POST'])
def admin(action):
	films = my_api.get_films()
	selections = my_api.populate_field_selection()
	ratings = selections['distinct_ratings']
	genres = selections['distinct_genres']
	error = ''
	form = DetailsForm()

	if request.method == 'POST':
		word_to_lookup = form.word_to_lookup.data
		film_id = form.film_id.data
		title = form.title.data
		year_released = form.year_released.data
		rating = form.rating.data
		genre = form.genre.data

		for num, distinct_genre in enumerate(genres, 1):
			if genre == str(num):
				genre = distinct_genre

		duration = form.duration.data
		fieldname = form.fieldname.data
		fieldvalue = form.fieldvalue.data

		if fieldname == 'genre':
			for num, distinct_genre in enumerate(genres, 1):
				if fieldvalue == str(num):
					fieldvalue = distinct_genre

		id_to_delete = form.id_to_delete.data

		# CREATE
		if title and year_released and rating and genre and duration:

			add = {"title": str(title), "duration": str(duration), "rating": str(rating), "genre": str(genre), "year_released": str(year_released)}
			print(add)
			confirm = my_api.add_film(add)
		
		# UPDATE
		elif film_id and fieldname and fieldvalue:
			update = {"film_id": str(film_id), "fieldname": str(fieldname), "fieldvalue": str(fieldvalue)}
			print(update)
			confirm = my_api.update_film(update)

		# READ
		elif word_to_lookup:
			check = {"word": str(word_to_lookup)}
			confirm = my_api.check_film(check)

		# DELETE
		elif id_to_delete:
			id_to_delete = str(id_to_delete)
			confirm = my_api.delete_film(id_to_delete)

		else:
			error = 'Incomplete Information not submitted'
			confirm = ''
		films = my_api.get_films()
		return render_template('admin.html', form=form, films=films, message=error, confirmation=confirm)
		 
	return render_template('admin.html', form=form, films=films, message=error, confirmation='', ratings=ratings, genres=genres, action=action, year=year)