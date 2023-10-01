## Web GUI Flask App

This flask App, deployed on Render, connects to my RestAPI to allow CRUD perations to be performed on a database of films in SQLite.

# [Web GUI Flask App](https://filmflixui.onrender.com/)
_Render does take a minute to spin up because I use the free service_

# [RestAPI](https://github.com/annwyl21/FilmFlixRestAPI)

### Database Integrity
- Dynamically generated lists are used for data entry to help ensure data integrity
- Several Layers of data validation:
	- HTML validation of user entered data
	- Validation checks within the RestAPI that runs when data is received as json
	- The validation in the RestAPI is checked with tests that run automatically on pull request, to ensure there is always working code in the RestAPI
	- RestAPI uses parameterized queries to ensure user input is always treated as data and not as executable code

