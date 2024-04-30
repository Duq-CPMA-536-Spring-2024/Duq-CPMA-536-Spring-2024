from flask import Flask, request, jsonify
from waitress import serve

from flask import Flask, send_from_directory, abort
from waitress import serve
import logging
import json
import os

from album_search import *

app = Flask(__name__)

@app.route('/')
def server_home_page():
    return "This is the server's home page. Nothing interesting to see here."

@app.route('/play/<album>/<track>')
#Use the following url to play the tracks within the albums.e %20 for space
# :http://127.0.0.1:5000/play/Album%203/Track%204.mp3
#For example: The above url will play track 4 from album 3.
def play_song(album, track):
    try:
        # Use send_from_directory to serve the MP3 file
        return send_from_directory(f'Music/{album}', track)
    except FileNotFoundError:
        return abort(404)  # Not found if file doesn't exist

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
    # Create an empty dictionary for all albums
    all_albums = {}

    # Relative path to the music directory with albums
    directory_name = 'Music'

    # Remove the .DS_Store folder if it exists
    album_list = os.listdir(directory_name)
    if '.DS_Store' in album_list:
        album_list.remove('.DS_Store')

    # Loop through the albums
    for album in album_list:
        # Get the list of tracks
        specific_album = get_album(album)
        # Add tracks to the dictionary with the albums
        all_albums[album] = specific_album

    # Return the list of the albums and album contents on the server
    return json.dumps(all_albums)

@app.route('/specific_album')
def specific_album():
    # This will return a list of tracks from a specified album.

    # Create a variable for the input of the specified album from the URL
    album_name = request.args.get('album_name', default='*', type=str)
    # URL: http://localhost:9999/specific_album?album_name=Album+1

    # Return the list of tracks for the album
    return get_album(album_name)

def get_album(name_of_album):
    # This will allow for reuse of code between task1 and task2 as appropriate

    # Relative path to the music directory with albums
    directory_name = 'Music'

    # Check if the 'Music' directory exists
    if not os.path.isdir(directory_name):
        return "Music folder not found."

    # Construct the path to the specific album
    album_path = os.path.join(directory_name, name_of_album)

    # Check if the directory specified by album_path exists
    if name_of_album == "" or not os.path.isdir(album_path):
        return "No such album exists."
    else:
        # Initialize an empty list of tracks
        tracks = []
        # List all tracks in the current album directory
        for track in os.listdir(album_path):
            if os.path.isfile(os.path.join(album_path, track)):
                # Add the track to the list
                tracks.append(track)

    # Return the list of tracks on the specified album
    return tracks


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