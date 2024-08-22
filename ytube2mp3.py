import os
import yt_dlp as youtube_dl  # Use yt-dlp instead of youtube_dl

# Function to download and convert video to MP3
def download_video(url, output_directory):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_directory, '%(title)s.%(ext)s'),
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '320'}],
        'verbose': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.96 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-us,en;q=0.5',
            'Sec-Fetch-Mode': 'navigate'
        }
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_output_path = ydl.prepare_filename(info_dict)
        return video_output_path
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Main function
def main():
    # YouTube video URL
    youtube_url = "https://youtu.be/XYb_hcIpYwQ"

    # Output directory
    output_directory = "/Users/tjv/Music"
    os.makedirs(output_directory, exist_ok=True)

    # Download the video and convert to MP3
    video_output_path = download_video(youtube_url, output_directory)
    if video_output_path:
        print(f"Video downloaded and converted to MP3: {video_output_path}")
    else:
        print("Failed to download or convert the video.")

if __name__ == "__main__":
    main()
