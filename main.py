import yt_dlp
import subprocess

def download_video(video_url, output_path):
  command = f'yt-dlp -o "{output_path}/%(title)s.%(ext)s" {video_url} -S ext:mp4:m4a'

  subprocess.run(command, shell=True)

if __name__ == "__main__":
  video_url = input("Enter the Youtube video URL: ")
  output_path = "./youtubeVideos"

  download_video(video_url, output_path)