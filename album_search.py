from flask import Flask, jsonify, request
import thefuzz as thefuzz
import os
from music_server import *
import thefuzz as thefuzz
from thefuzz import process
#import fuzzywuzzy as fuzzywuzzy
#from fuzzywuzzy import process

app = Flask(__name__)


# Helper func for creating a list to be searched for with fuzzy search
def list_albums(music_directory):
    """
    :param music_directory is a specified path to a directory
    :return: list of album names from subdirectories names or raise an error if DNE

    """
    # check/handles invalid parameter entries for directory name and path
    if not os.path.exists(music_directory):
        raise ValueError(f"Directory -> {music_directory} DNE")
    if not os.path.isdir(music_directory):
        raise ValueError(f"Path -> {music_directory} is not a directory ")

    # return with list comprehension
    return [name for name in os.listdir(music_directory)
            if os.path.isdir(os.path.join(music_directory, name))
            ]

def fuzzy_search_albums(query, music_dir):
    """
    :param query is the search entry
    :param music_dir is the path to the directory holding subdir names as album titles
    :return: match with query search and album in music directory list as well as
    an accuracy score of how well the response matches the query
    """
    albums = list_albums(music_dir)
    matches = process.extract(query, albums, limit=1)      # given some query, list of albums, and a constraint for the number of responses for the search
    return matches                                          # list of matches generated from fuzzywuzzy




