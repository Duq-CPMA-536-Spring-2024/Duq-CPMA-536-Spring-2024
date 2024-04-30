from flask import Flask, jsonify, request
from album_search import *
from music_server import *
import thefuzz as thefuzz
import os
import thefuzz as thefuzz
from thefuzz import process
#import fuzzywuzzy as fuzzywuzzy
#from fuzzywuzzy import process

SEARCH_FOLDER_PATH = r"C:\Users\davis_g7\OneDrive\Documents\Duq-CPMA-536-Spring-2024\Music"
# Helper func for creating a list to be searched for with fuzzy search
app = Flask(__name__)

def list_songs(album_directory):
    """
    :param music_directory is a specified path to a directory
    :return: list of album names from subdirectories names or raise an error if DNE

    """
    # check/handles invalid parameter entries for directory name and path
    if not os.path.exists(album_directory):
        raise ValueError(f"Music Directory -> {album_directory} DNE")
    if not os.path.isdir(album_directory):
        raise ValueError(f"Path -> {album_directory} is not a directory ")

    # may need to add this from app route
    song_duration = request.args.get('song_duration', '').lower()
    search_song = request.args.get('song_search', '').lower()
    search_album = request.args.get('album_search', '').lower()

    album_path = fuzzy_search_albums(search_album, SEARCH_FOLDER_PATH)
    song_path = fuzzy_search_albums(search_song, SEARCH_FOLDER_PATH)
    # if os.path.isdir(album_path):
    #     song = os.listdir(album_path)
    # else:
    #     song = []

    if os.path.isdir(song_path):
        song = os.listdir(album_path)
    else:
        song = []


def fuzzy_search_songs(query, album_dir):
    """
    :param query is the search entry
    :param music_dir is the path to the directory holding subdir names as album titles
    :return: match with query search and album in music directory list as well as
    an accuracy score of how well the response matches the query
    """
    song = list_songs(album_dir)
    matches = process.extract(query, song, limit=1)      # given some query, list of albums, and a constraint for the number of responses for the search

    return matches # list of matches generated from fuzzywuzzy