from song_duration import *
from flask import Flask, jsonify, request
import album_search
import os
from waitress import serve
import logging
import json


app = Flask(__name__)

SEARCH_FOLDER_PATH = r"C:\Users\davis_g7\OneDrive\Documents\Duq-CPMA-536-Spring-2024\Music"
#SEARCH_FOLDER_PATH = r"C:\insert\path\to\your\music\directory\here"

# URL's for accessing server
# http://localhost:9999/search_album?album_name=Album+1
# http://localhost:9999/search_album?album_name=Album%201
# http://localhost:9999/search_album?album_name=YourSearchQuery



@app.route('/search_album', methods=['GET'])
def search_album():
	"""
	Builds a query with request object
	The object contains parameters such as data, query parameters, files, and URL
	The request object is then passed to the fuzzy_search_albums function from the
	album_search file in addition to the specified path of the directory

	returns: array from the search 'match' var, is wrapped/encapsulated as a JSON object with jsonify()
	"""
	# search path var should be defined outside of endpoint configuration
	#SEARCH_FOLDER_PATH = r"C:\Users\davis_g7\OneDrive\Documents\Duq-CPMA-536-Spring-2024\Music"
	search = request.args.get('album_search', '').lower()
	# Assuming fuzzy_search_albums is defined elsewhere and properly imported
	match = album_search.fuzzy_search_albums(search, SEARCH_FOLDER_PATH)
	return jsonify(match)


@app.route('/search_song', methods=['GET'])
def search_song():
	"""
	Builds a query with request object
	The object contains parameters such as data, query parameters, files, and URL
	The request object is then passed to the fuzzy_search_albums function from the
	album_search file in addition to the specified path of the directory

	returns: array from the search 'match' var, is wrapped/encapsulated as a JSON object with jsonify()
	"""
	# search path var should be defined outside of endpoint configuration
	#SEARCH_FOLDER_PATH = r"C:\Users\davis_g7\OneDrive\Documents\Duq-CPMA-536-Spring-2024\Music"
	search = request.args.get('album_song', '').lower()
	# Assuming fuzzy_search_albums is defined elsewhere and properly imported
	match_song = fuzzy_search_songs(search, SEARCH_FOLDER_PATH)
	return jsonify(match_song)


@app.route('/')
def server_home_page():
	return "This is the server's home page. Nothing interesting to see here."

@app.errorhandler(Exception)
def page_not_found(e):
	print(e)
	return '404 Not Found', 404

@app.route('/specific_album')
def specific_album():
	# This will return a list of tracks from a specified album.

	# Create a variable for the input of the specified album from the URL
	album_name = request.args.get('album_name', default='*', type=str)
	# URL: http://localhost:9999/specific_album?album_name=Album+1

	# Initialize an empty dictionary to store the album and its tracks
	specific_album = {}

	# Relative path to the Music directory with Albums
	directory_name = 'Music'

	# Construct the path to the specific album
	album_path = os.path.join(directory_name, album_name)

	# Check if the directory specified by album_path exists
	if album_name == "":
		return "No such album exists."
	elif os.path.isdir(album_path):
		# Initialize an empty list of tracks
		tracks = []
		# List all tracks in the current album directory
		for track in os.listdir(album_path):
			if os.path.isfile(os.path.join(album_path, track)):
				tracks.append(track)
		# Add album and its tracks to album dictionary
		specific_album[album_name] = tracks
	else:
		# The album does not exist
		return "No such album exists."

	# Return the list of tracks on the specified album
	return json.dumps(specific_album)

if __name__ == '__main__':
	logging.getLogger('waitress').setLevel(logging.DEBUG)
	serve(app, host='0.0.0.0', port=9999)