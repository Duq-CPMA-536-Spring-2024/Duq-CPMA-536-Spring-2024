from mutagen.mp3 import MP3

song_path = 'Music'
# source https://dev.to/konyu/how-to-get-mp3-file-s-durations-with-python-42p
def mutagen_length(path):
    try:
        audio = MP3(path)
        length = audio.info.length
        return length
    except:
        return length
