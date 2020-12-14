# this module will be for processing and comparing the images of each frame
# Steps: Need to figure out an arbitrary threshold value formula for each video and stream
# that gets processed in order to accurately compare and filter images based on each specific video
import shutil
import os
import cv2
import numpy as np

def filterFrames(video):
    print("Entering filterFrames function")

    # for loop to convert images to greyscale
    # directory = os.listdir(os.getcwd() + '/stored_files/data/')
    directory = os.listdir('data')

    # for image in os.listdir("data/"):
    for image in directory:
        img = cv2.imread(image)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Employ rectangular border detection






def createSheetMusic():
    print("Create Sheet Music")


def destroyStoredFrames():
    print("Destroying stored frames now that PDF has been created.")
    shutil.rmtree('data')
