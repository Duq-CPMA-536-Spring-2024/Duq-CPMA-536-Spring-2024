from flask import Flask, send_file
from waitress import serve
import os
import random
import logging

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

@app.route('/')
def server_home_page():
	return "This is the server's home page. Nothing interesting to see here."



@app.errorhandler(Exception)
def page_not_found(e):
    print(e)
    return '404 Not Found', 404


if __name__ == '__main__':
    logging.getLogger('waitress').setLevel(logging.DEBUG)
    serve(app, host='0.0.0.0', port=9999)
