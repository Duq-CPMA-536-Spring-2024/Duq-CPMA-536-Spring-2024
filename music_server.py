from flask import Flask, send_file, request
from waitress import serve
import os
import random
import logging
import json

app = Flask(__name__)


def selectRandomSong(rootFolder):
    # albumFolder has the list of sub folders
    albumFolders = [f.path for f in os.scandir(rootFolder) if f.is_dir()]
    # We are selecting the folder here
    randomAlbumFolder = random.choice(albumFolders)
    # Listing the mp3 files
    mp3Files = [f.path for f in os.scandir(randomAlbumFolder) if f.is_file() and f.name.endswith('.mp3')]
    # We are selecting mp3 file
    random_mp3_file = random.choice(mp3Files)
    return random_mp3_file


@app.route('/playRandomSong')
def playRandomSong():
    # Select a random song
    random_song = selectRandomSong('Music')

    # Return the selected song for playback in the browser
    return send_file(random_song, mimetype='audio/mpeg')

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
