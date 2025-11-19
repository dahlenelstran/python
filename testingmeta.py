import yt_dlp
import os
# from mutagen.easyid3 import EasyID3
from mutagen.mp3 import EasyMP3 as MP3

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

# def add_meta(folder, album, artist):
#     track_num = 1
#     for file in os.listdir(folder): 
#         if file.endswith(".mp3"): 
#             file_path = os.path.join(folder, file) 
#             try: 
#                 audio = EasyID3(file_path)
#             except: audio = EasyID3() 
#             audio['album'] = album 
#             audio['artist'] = artist 
#             audio['title'] = file.replace('.mp3', '') 
#             audio.save()
#             print("Edited Metadata for " + album + str(track_num))
#             track_num += 1

def add_meta(folder, album, artist):
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        


if __name__ == "__main__":

    artist = input("Enter album artist: ")
    album = input("Enter album title: ")
    folder = os.path.join(os.getcwd(), artist , album)
    add_meta(folder, album, artist)