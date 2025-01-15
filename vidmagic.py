import yt_dlp
import os

# obtener ruta de descargas
def get_downloads_folder():
    if os.name == 'nt':  # alternative windows
        from winreg import OpenKey, QueryValueEx, HKEY_CURRENT_USER
        sub_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
        with OpenKey(HKEY_CURRENT_USER, sub_key) as key:
            downloads_path = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
    else:  # alternative linux o mac 
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    return downloads_path

SAVE_PATH = get_downloads_folder()

# option mp4
def download_video(link):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{SAVE_PATH}/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

# option mp3
def download_audio(link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{SAVE_PATH}/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

# main principal
if __name__ == "__main__":
    print("🎥 Welcome to the Video Downloader 🎶")
    print("====================================\n")

    link = input("🌐 Enter the video link: ")

    print("\nChoose your preferred format:")
    print("1️⃣ MP4 (Video)")
    print("2️⃣ MP3 (Audio)")
    option = int(input("\n🔷 Your choice (1 or 2): "))

    if option == 1:
        download_video(link)
    elif option == 2:
        download_audio(link)