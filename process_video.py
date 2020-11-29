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

    # make sure the same youtube video isn't being downloaded (causes infinite download)
    # if find(file.title, os.path.join(os.getcwd(), 'stored_files')) is True:
    #    sys.exit('This file has already been downloaded')
    # else:

    stream.download('stored_files'),
    print("Finished downloading video into directory")


def frame_capture(path):
    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable
    count = 0

    # checks whether frames were extracted
    success = 1

    while success:
        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()

        # Saves the frames with frame-count
        # cv2.imwrite("frame%d.jpg" % count, image)

        count += 1


def find(name, path):
    # helper function to identify if a video has already been downloaded into directory
    for root, dirs, files in os.walk(path):
        if name in files:
            return True
