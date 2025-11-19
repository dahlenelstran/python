import yt_dlp
import os
from mutagen.easyid3 import EasyID3

# command line that worked:
# yt-dlp -t mp3 "https://music.youtube.com/watch?v=a3JSbOt7CLo&si=Nugjl0hhYhe4O8Sc" --cookies-from-browser firefox

def download(url, folder):
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'audioformat': 'mp3',
        'outtmpl': f'{folder}/%(title)s.%(ext)s',
        'embedmetadata': True,
        'addmetadata': True,
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    if not os.path.exists(folder): 
        os.makedirs(folder)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(url)

# Get metadata from link

# I don't think this is doing a single thing

def add_meta(folder, album, artist):
    for file in os.listdir(folder): 
        if file.endswith(".mp3"): 
            file_path = os.path.join(folder, file) 
            try: 
                audio = EasyID3(file_path)
            except: audio = EasyID3() 
            audio['album'] = album 
            audio['artist'] = artist 
            audio['title'] = file.replace('.mp3', '') 
            audio.save() 

if __name__ == "__main__":

    option = 0
    while option == 0:
        option = int(input("Enter 1 for song, 2 for album, 3 for playlist: "))
        if option == 1:
            url = input("Enter song URL: ")
            artist = input("Enter song artist: ")
            album = input("Enter song album: ")
            folder = os.path.join(os.getcwd(), artist , album)
            download(url, folder)
            add_meta(folder, album, artist)
        elif option == 2: 
            url = input("Enter album URL: ")
            artist = input("Enter album artist: ")
            album = input("Enter album title: ")
            folder = os.path.join(os.getcwd(), artist , album)
            download(url, folder)
            add_meta(folder, album, artist)
        elif option == 3: 
            url = input("Enter playlist URL: ")
            title = input("Enter playlist title: ")
            folder = os.path.join(os.getcwd(), title)
            download(url, folder)
        else:
            option = 0
            print("Option out of range, please try again.")

