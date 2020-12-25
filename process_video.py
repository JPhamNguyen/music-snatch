import cv2
from pytube import YouTube
import sys
import os
import process_images
import numpy as np


def store_video(vid):
    # if not already downloaded, store video into a specific directory
    file = YouTube(vid)
    # filter for a stream with 1080p and a mp4 format
    stream = file.streams.filter(res='1080p', mime_type='video/mp4').first()

    # check for existing directories for storing files + images
    # print(os.getcwd())

    if not os.path.exists(os.path.join(os.getcwd(), 'stored_files')):
        print("create a new directory to store YouTube videos + files")
        os.mkdir('stored_files')

    stream.download('stored_files')
    print("Finished downloading video into directory")
    return file.title


def frame_capture(video):
    # Splits video into frames to be analyzed later
    path = os.getcwd() + '/stored_files/' + str(video)
    print(video)
    cap = cv2.VideoCapture(path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(length)

    frames_data = 'data/' + video
    print(frames_data)
    try:
        if not os.path.exists(frames_data):
            os.makedirs('data')
    except OSError:
        print('Error: Creating directory of data')

    # iterate over video's frames and store them as greyscale images
    currentFrame = 0
    previousFrame = ''
    # while True:
    while currentFrame != length:
        # read image
        ret, frame = cap.read()

        # isolate sheet music from video frame
        frame = process_images.isolateSheetMusic(frame)

        if currentFrame == 0:
            name = './data/frame' + str(currentFrame) + '.jpg'
            print('Creating...' + name)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(name, frame)
            currentFrame += 1
            previousFrame = frame
        # else:
            # bool value to describe if two images are duplicates
            # duplicate = process_images.compareFrames(frame, previousFrame)
            # if duplicate is True:
                # pass
            # else:
                # name = './data/frame' + str(currentFrame) + '.jpg'
                # print('Creating...' + name)
                # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # cv2.imwrite(name, frame)
                # currentFrame += 1
                # previousFrame = frame

    cap.release()
    cv2.destroyAllWindows()


def processMetadata(video):
    print("intended to return important timestamps and data")


def find(name, path):
    # helper function to identify if a video has already been downloaded into directory
    for root, dirs, files in os.walk(path):
        if name in files:
            return True
