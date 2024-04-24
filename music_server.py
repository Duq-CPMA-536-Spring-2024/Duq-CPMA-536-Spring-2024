
from flask import Flask, request, jsonify, send_from_directory

import os

from waitress import serve

import logging

app = Flask(__name__)
app.config['MEDIA_FOLDER'] = os.path.join(os.getcwd(), 'Music')
@app.route('/')
def server_home_page():
	return "This is the server's home page. Nothing interesting to see here."
@app.route('/playback', methods=['GET'])
def play_song():
    album = request.args.get('album')
    song = request.args.get('song')
    if not album or not song:
        return jsonify({"error": "Missing required parameters"}), 400

    # Construct the path to the song
    song_path = os.path.join(app.config['MEDIA_FOLDER'], album, song)

    # Check if the file exists
    if not os.path.isfile(song_path):
        return jsonify({"error": "File not found"}), 404

    # Send the file for download or streaming
    return send_from_directory(directory=os.path.join(app.config['MEDIA_FOLDER'], album), filename=song, as_attachment=False)

    # Check if the file exists
    if not os.path.isfile(os.path.join(track_path, track)):
        return jsonify({"error": "File not found"}), 404

    # Serve the Track file to be played in the browser
    return send_from_directory(directory=track_path, filename=track , as_attachment=False)
@app.errorhandler(Exception)
def page_not_found(e):
	print(e)
	return '404 Not Found', 404

@app.errorhandler(Exception)
def page_not_found(e):
	print(e)
	return '404 Not Found', 404

if __name__ == '__main__':
	logging.getLogger('waitress').setLevel(logging.DEBUG)
	serve(app, host='0.0.0.0', port=9999)