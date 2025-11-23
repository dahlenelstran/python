import os 
import yt_dlp 
from mutagen.mp3 import EasyMP3

def download_youtube_playlist_as_mp3(playlist_url, output_folder): 
    # Ensure the output folder exists 
    if not os.path.exists(output_folder): 
        os.makedirs(output_folder) 
        # yt-dlp configuration for audio extraction 
        ydl_opts = { 
            'format': 'bestaudio/best', 
            'ffmpeg_location': '/usr/local/bin/ffmpeg', # macbook
            'ffprobe_location': '/usr/local/bin/ffprobe', #macbook
            'outtmpl': f'{output_folder}/%(artist)s/%(album)s/%(title)s.%(ext)s', 
            # Save to artist/album/Title.mp3 
            'extractaudio': True, # Extract audio only 
            'audioformat': 'mp3', # Convert to MP3 
            'noplaylist': False, # Enable downloading the whole playlist 
            'quiet': False, # Show progress 
            'cookies_from_browser': 'firefox', 
            'postprocessors': [{ 
                'key': 'FFmpegExtractAudio', 
                'preferredcodec': 'mp3', 
                'preferredquality': '192', # MP3 audio quality 
                }], 
            } 
        # Download playlist 
        with yt_dlp.YoutubeDL(ydl_opts) as ydl: 
            print(f"Downloading playlist: {playlist_url}") 
            ydl.download([playlist_url]) 
            print(f"All files downloaded to {output_folder}") 
            
def add_metadata_to_mp3(mp3_folder, album_name, artist_name): 
    # Add metadata to all MP3 files in the folder 
    for file in os.listdir(mp3_folder): 
        if file.endswith(".mp3"): 
            file_path = os.path.join(mp3_folder, file) 
            try: 
                audio = EasyMP3(file_path) 
                print(f"Automatically edited metadata") 
            except: 
                audio = EasyMP3() 
                audio['album'] = album_name 
                audio['artist'] = artist_name 
                audio['title'] = file.replace('.mp3', '') 
                audio.save() 
                print(f"Manually edited metadata") 
        
if __name__ == "__main__": 
    playlist_link = input("Enter the YouTube playlist URL: ") 
    album_name = input("Enter the album name: ") 
    artist_name = input("Enter the artist name: ") 
    output_directory = os.path.join(os.getcwd(), album_name)
    # Save in current dir with album name 
    # Step 1: Download audio 
    download_youtube_playlist_as_mp3(playlist_link, output_directory) 
    # Step 2: Add metadata 
    add_metadata_to_mp3(output_directory, album_name, artist_name)
    print("Download and metadata tagging complete!")