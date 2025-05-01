import yt_dlp

def download_youtube_video(video_url, download_path="./videos"):
    """
    Downloads a YouTube video using yt-dlp.

    Args:
        video_url (str): The URL of the YouTube video.
        download_path (str): The directory where the video will be saved.

    Returns:
        None
    """
    try:
        ydl_opts = {
            'outtmpl': f'{download_path}/%(title)s.%(ext)s',  # Save video with title as filename
            'format': 'best',  # Download the best video + audio quality
        }

        # Create videos directory if it doesn't exist
        import os
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        # Download video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from {video_url}...")
            ydl.download([video_url])
            print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ").strip()
    download_path = input("Enter the download path (leave empty for './videos'): ").strip() or "./videos"
    download_youtube_video(video_url, download_path)
