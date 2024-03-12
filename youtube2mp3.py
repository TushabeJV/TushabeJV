import os
import moviepy.editor as mp
from pytube import YouTube

# Function to download YouTube video
def download_video(url, output_directory):
    yt = YouTube(url)
    ys = yt.streams.filter(only_audio=False).first()
    video_output_path = os.path.join(output_directory, "/Users/tjv/PycharmProjects/myStuff_jv/song1.mp4")  # Set the output file path
    ys.download(output_path=output_directory, filename="song1.mp4")  # Specify the filename with .mp4 extension
    return video_output_path  # Return the full path to the downloaded video

# Function to convert video to MP3
def video_to_mp3(video_path, mp3_path, target_fps=30):
    audio_clip = mp.AudioFileClip(video_path)
    audio_clip.write_audiofile(mp3_path)


# Main function
def main():
    # YouTube video URL
    youtube_url = "https://www.youtube.com/watch?v=1KRVzf-hOnQ"

    # Output directory
    output_directory = "/Users/tjv/PycharmProjects/myStuff_jv"
    os.makedirs(output_directory, exist_ok=True)

    # Download the video and get the full path
    video_output_path = download_video(youtube_url, output_directory)

    # Convert the video to MP3
    mp3_output_path = os.path.join(output_directory, "Make a way.mp3")
    video_to_mp3(video_output_path, mp3_output_path)

    print(f"Video downloaded and converted to MP3: {mp3_output_path}")

if __name__ == "__main__":
    main()



