import librosa
import mutagen
from mutagen.mp3 import MP3
import os
from flask import jsonify

def get_track_length(song_path):
    """
    Retrieve the length of the track specified by the given path
    Uses librosa library to calculate the duration
    """
    if not song_path:
        return jsonify({'error': 'File path parameter is missing'})

    if not os.path.isfile(song_path):
        return jsonify({'error': 'File does not exist or is not a valid file'})

    # try-except block
    try:
        # Load audio file with its sampling rate (sr=None)
        y, sr = librosa.load(song_path, sr=None)
        # Calculate the track length in seconds
        track_length = librosa.get_duration(y=y, sr=sr)
        return jsonify({'length_in_seconds': track_length})

    except Exception as err:
    #     # Handle errors during processing
         return jsonify({'error': str(err)})

song_path = r"C:\Users\davis_g7\OneDrive\Documents\Duq-CPMA-536-Spring-2024\Music\Album 2\Track 2.mp3"
# source https://dev.to/konyu/how-to-get-mp3-file-s-durations-with-python-42p
def mutagen_length(path):
    try:
        audio = MP3(path)
        length = audio.info.length
        return length
    except:
        return length

#length = mutagen_length(song_path)
#print(str(length))
#print("duration sec: " + str(length))
#print("duration min: " + str(int(lengxth/60)) + ':' + str(int(length%60)))