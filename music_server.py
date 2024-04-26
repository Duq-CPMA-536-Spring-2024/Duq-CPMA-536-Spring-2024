
from flask import Flask, send_from_directory, abort
import os
from waitress import serve
import logging

app = Flask(__name__)
# Set the path to the music folder in the working directory
app.config['MEDIA_FOLDER'] = os.path.join(os.getcwd(), 'Music')
@app.route('/')
def server_home_page():
	return "This is the server's home page. Nothing interesting to see here."
@app.route('/play/<album>/<track>')
#Use the following url to play the tracks within the albums.e %20 for space
# :http://127.0.0.1:5000/play/Album%203/Track%204.mp3
#For example: The above url will play track 4 from album 3.
def play_song(album, track):
    # Sanitize input to match directory and file naming conventions
    valid_albums = ['Album 1', 'Album 2', 'Album 3']
    album = ' '.join([word.capitalize() for word in album.split('_')])

    if album not in valid_albums or not track.endswith('.mp3'):
        return abort(404)  # Not found if invalid album or track

    try:
        # Use send_from_directory to serve the MP3 file
        return send_from_directory(f'Music/{album}', track)
    except FileNotFoundError:
        return abort(404)  # Not found if file doesn't exist
@app.errorhandler(Exception)
def page_not_found(e):
	print(e)
	return '404 Not Found', 404

if __name__ == '__main__':
	logging.getLogger('waitress').setLevel(logging.DEBUG)
	serve(app, host='0.0.0.0', port=9999)