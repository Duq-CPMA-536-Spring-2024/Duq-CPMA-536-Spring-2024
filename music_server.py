from flask import Flask, request, jsonify
from waitress import serve

import logging
import json
import os

from album_search import *

app = Flask(__name__)

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


SEARCH_FOLDER_PATH = r"C:\Users\davis_g7\OneDrive\Documents\Duq-CPMA-536-Spring-2024\Music"
#SEARCH_FOLDER_PATH = r"Music"

#http://localhost:9999/search_album?album_name=YourSearchQuery
#http://localhost:9999/search_album?album_name=Album%201

@app.route('/search_album', methods=['GET'])
def search_album():
    """
    Builds query with Flask request object
	match var is generated from source file album_search.py fuzzy_search_albums()
    """
    search = request.args.get('album_name', '').lower()
    # Assuming fuzzy_search_albums is defined elsewhere and properly imported
    match = fuzzy_search_albums(search, SEARCH_FOLDER_PATH)
    return jsonify(match)


if __name__ == '__main__':
	logging.getLogger('waitress').setLevel(logging.DEBUG)
	serve(app, host='0.0.0.0', port=9999)