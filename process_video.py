import cv2
from pytube import YouTube
import sys
import os


def store_video(vid):
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
    # Path to video file
    path = os.getcwd() + '/stored_files/' + str(video)
    print(video)
    cap = cv2.VideoCapture(path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(length)

    frames_data = 'data/' + video
    print(frames_data)
    try:
        # if not os.path.exists('data/' + video):
        if not os.path.exists(frames_data):
            os.makedirs('data')
    except OSError:
        print('Error: Creating directory of data')

    currentFrame = 0
    # while True:
    while currentFrame != length:
        ret, frame = cap.read()

        name = './data/frame' + str(currentFrame) + '.jpg'
        print('Creating...' + name)
        cv2.imwrite(name, frame)
        currentFrame += 1

    cap.release()
    cv2.destroyAllWindows()


def find(name, path):
    # helper function to identify if a video has already been downloaded into directory
    for root, dirs, files in os.walk(path):
        if name in files:
            return True
