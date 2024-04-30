from flask import Flask, request
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
    # Create an empty dictionary for all albums
    all_albums = {}

    directory_name = 'Music'

    album_list = os.listdir(directory_name)
    if '.DS_Store' in album_list:
        album_list.remove('.DS_Store')

    # Loop through the albums
    for album in album_list:
        specific_album = get_album(album)
        all_albums[album] = specific_album

    # Return the list of the albums and album contents on the server
    return json.dumps(all_albums)


@app.route('/specific_album')
def specific_album():
    # This will return a list of tracks from a specified album.

    # Create a variable for the input of the specified album from the URL
    album_name = request.args.get('album_name', default='*', type=str)
    # URL: http://localhost:9999/specific_album?album_name=Album+1

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
                tracks.append(track)

    # Return the list of tracks on the specified album
    return tracks


if __name__ == '__main__':
    logging.getLogger('waitress').setLevel(logging.DEBUG)
    serve(app, host='0.0.0.0', port=9999)