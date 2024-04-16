from flask import Flask, request, jsonify
from thefuzz import process
from waitress import serve
import logging
import os


app = Flask(__name__)
#@app.route('search album', methods=['GET'])
#def search_album():

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