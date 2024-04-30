# album_search.py
import os
from thefuzz import process

def list_albums(music_dir):
    """
    :param passed in path to music directory
    Lists all subdirectories in the given music directory
    Each subdirectory represents an album
    :returns the list of albums
    """

    # list comprehension of subdirectories of albums
    return [name for name in os.listdir(music_dir)
            if os.path.isdir(os.path.join(music_dir, name))
            ]

# Uses list from directory to build fuzzy search func
def fuzzy_search_albums(query, music_dir):
    """
    :param query as search entry, music_dir given location of album subdirectories
    takes passed in args, uses the above defined list_albums function (that returns a list of albums) as passes them and
    generates fuzzy search with process.extract()
    :return the most accurate comparison/match it finds within the given destination
    """

    albums = list_albums(music_dir)
    matches = process.extract(query, albums, limit=3)      # given some query, list of albums, and a constraint for the number of responses for the search
    return matches                                         # list of matches generated from thefuzz


