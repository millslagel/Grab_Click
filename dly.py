import os
from pytube import YouTube
from moviepy.editor import *

# Set the URL of the YouTube video you want to download
#url = 'https://www.youtube.com/watch?v=tUCRjB1OUF0'
url = input('Enter YouTube URL:\n')

# Create a YouTube object
yt = YouTube(url)

# Set the filename and format (mp3 in this case)
audio = yt.streams.filter(only_audio=True).first()

# Download the video
audio.download()

directory = os.getcwd()

mp4_file = [f for f in os.listdir(directory) if f.endswith('.mp4')]

hold = mp4_file[0]

print (hold)

test = input('Enter to continue:\n')

# Load the mp4 file
clip = AudioFileClip(hold)

# Extract audio from video
clip.write_audiofile((hold[:-4]) + ".mp3")

clip.close()

os.remove(hold)

