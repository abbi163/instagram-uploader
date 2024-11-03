import os  # For environment variable access
import pandas as pd
from datetime import datetime
from instagrapi import Client


def upload_video_and_story(video_path, caption):
    """
    Uploads a video to Instagram as both a post and a story.

    Parameters:
    video_path (str): The file path of the video to upload.
    caption (str): The caption to include with the post.
    """
    # Initialize the Instagram client
    cl = Client()

    # Login using stored credentials or provide a secure way to authenticate
    cl.login(os.getenv('INSTAGRAM_USERNAME'), os.getenv('INSTAGRAM_PASSWORD'))

    # Upload the video as a post
    cl.video_upload(video_path, caption)
    print(f"Video uploaded as a post with caption: {caption}")

    # Upload the video as a story
    cl.video_upload_to_story(video_path)
    print("Video uploaded as a story")


# Load the schedule from the CSV file
schedule_csv_path = 'media_schedule.csv'
schedule_df = pd.read_csv(schedule_csv_path)

# Get today's date
today_date = datetime.now().strftime('%Y-%m-%d')

# Check if there is a media file for today
media_row = schedule_df[schedule_df['Date'] == today_date]

if not media_row.empty:
    media_path = media_row.iloc[0]['File Path']

    # Read the caption from caption.txt
    with open('caption.txt', 'r') as caption_file:
        caption = caption_file.read().strip()
    # Upload the media if found
    upload_video_and_story(media_path, caption)
else:
    print("No media scheduled for today")
