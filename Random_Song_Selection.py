import os
import random
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

