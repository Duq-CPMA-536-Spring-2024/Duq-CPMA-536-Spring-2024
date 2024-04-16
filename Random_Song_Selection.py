import os
import random
def selectRandomSong(rootFolder):
    albumFolders = [f.path for f in os.scandir(rootFolder) if f.is_dir()]
    randomAlbumFolder = random.choice(albumFolders)
    mp3Files = [f.path for f in os.scandir(randomAlbumFolder) if f.is_file() and f.name.endswith('.mp3')]
    random_mp3_file = random.choice(mp3Files)
    return random_mp3_file


def main():
    rootFolder = "C:\\Users\\Niteesh\Documents\Duq-CPMA-536-Spring-2024\Music"
    randomSong = selectRandomSong(rootFolder)
    print("Randomly selected song:", randomSong)

if __name__ == "__main__":
    main()
