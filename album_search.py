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
    :param musicDirectory:
    :return: list of album names from subdirectories names

    """
    # list comprehension return
    return [name for name in os.listdir(music_directory)
            if os.path.isdir(os.path.join(music_directory, name))
            ]

# Uses list from directory to build fuzzy search func
def fuzzy_search_albums(query, music_dir):
    """
    :param query: search entry
    :param music_dir is the path to the directory holding subdir as albums
    :return: match with query search and album in music directory list as well as
    an accuracy score of how well the response matches the query
    """
    albums = list_albums(music_dir)
    matches = process.extract(query, albums, limit=3)      # given some query, list of albums, and a constraint for the number of responses for the search
    return matches



