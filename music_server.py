from flask import Flask
from waitress import serve

import logging
import json
import os

app = Flask(__name__)

@app.route('/')
def server_home_page():
	return "This is the server's home page. Nothing interesting to see here."

@app.errorhandler(Exception)
def page_not_found(e):
	print(e)
	return '404 Not Found', 404

@app.route('/allalbums')
def get_albums_with_tracks():
	"""
	Retrieve a complete list of albums and the contents
	of each album on the server.
	"""

	# Initialize an empty dictionary to store albums and their tracks
	albums={}

	# Relative path to the Music directory with Albums
	directory_name = 'Music'

	# Check if the 'Music' directory exists
	if not os.path.isdir(directory_name):
		return "Music folder not found."

	# Loop through the albums
	for album in os.listdir(directory_name):

		# Construct the path to the current album
		album_path = os.path.join(directory_name, album)

		# Check if the directory specified by album_path exists
		if os.path.isdir(album_path):

			# Initialize an empty list of tracks
			tracks = []
			# List all tracks in the current album directory
			for track in os.listdir(album_path):
				if os.path.isfile(os.path.join(album_path, track)):
					tracks.append(track)

			# Add album and its tracks to albums dictionary
			albums[album] = tracks

	# Return the list of the albums and album contents on the server
	return json.dumps(albums)


if __name__ == '__main__':
	logging.getLogger('waitress').setLevel(logging.DEBUG)
	serve(app, host='0.0.0.0', port=9999)