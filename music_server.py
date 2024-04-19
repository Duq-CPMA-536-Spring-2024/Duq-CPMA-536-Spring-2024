from flask import Flask, jsonify, request
from album_search import *
import os
from waitress import serve
import logging
from album_search import *

app = Flask(__name__)

SEARCH_FOLDER_PATH = r"C:\Users\davis_g7\OneDrive\Documents\Duq-CPMA-536-Spring-2024\Music"

@app.route('/search_album', methods=['GET'])
def search_album():
    """
    Builds a query with the request object
    The object contains parameters such as data, query parameters, files, and URL
    The request object is then passed to the fuzzy_search_albums function from the
    album_search file in addition to the specified path of the directory

    returns: array from the search 'match' var, is wrapped/encapsulated as a JSON object with jsonify()
    """
    search = request.args.get('album_name', '').lower()
    # Assuming fuzzy_search_albums is defined elsewhere and properly imported
    match = fuzzy_search_albums(search, SEARCH_FOLDER_PATH)
    return jsonify(match)

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


