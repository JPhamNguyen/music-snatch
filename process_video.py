import cv2
from pytube import YouTube
import sys
import os


def store_video(vid):
    file = YouTube(vid)
    print(file.title)
    # filter for a stream with 1080p and a mp4 format
    stream = file.streams.filter(res='1080p', mime_type='video/mp4').first()
    print(stream)

    # check for existing directories for storing files + images
    print(os.getcwd())

    if not os.path.exists(os.path.join(os.getcwd(), 'stored_files')):
        print("create a new directory to store YouTube videos + files")
        os.mkdir('stored_files')

    print("About to download")
    stream.download('stored_files')
    print("Done with downloading")
