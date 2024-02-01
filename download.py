import argparse
from pytube import YouTube

# Directories to save video and audio
VIDEO_SAVE_DIRECTORY = "./videos"
AUDIO_SAVE_DIRECTORY = "./audio"

def download(video_url):
    """
    Download highest resolution video stream.
    :param video_url: YouTube video URL
    """
    video = YouTube(video_url)
    video = video.streams.get_highest_resolution()

    try:
        video.download(VIDEO_SAVE_DIRECTORY)
        print("Video downloaded successfully")
    except Exception as e:
        print(f"Failed to download video: {e}")

def download_audio(video_url):
    """
    Download audio-only stream.
    :param video_url: YouTube video URL
    """
    video = YouTube(video_url)
    audio = video.streams.filter(only_audio=True).first()

    try:
        audio.download(AUDIO_SAVE_DIRECTORY)
        print("Audio downloaded successfully")
    except Exception as e:
        print(f"Failed to download audio: {e}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", required=True, help="URL to YouTube video")
    ap.add_argument("-a", "--audio", required=False, help="Download audio only", action="store_true")
    args = vars(ap.parse_args())

    if args["audio"]:
        download_audio(args["video"])
    else:
        download(args["video"])