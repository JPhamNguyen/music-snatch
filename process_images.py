# this module will be for processing and comparing the images of each frame
# Steps: Need to figure out an arbitrary threshold value formula for each video and stream
# that gets processed in order to accurately compare and filter images based on each specific video
import shutil
import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import imutils


def isolateSheetMusic(frame):
    # uses rectangular border detection for sheet music
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
    # cv2.imshow('blurred', blurred)
    # cv2.imshow('threshed', thresh)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    contours = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    for c in contours:
        m = cv2.moments(c)
        # cX = int((m["m10"] / m["m00"]))
        # cY = int((m["m01"] / m["m00"]))
        c = c.astype("float")
        c = c.astype("int")
        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        # show the output image
        # cv2.imshow("analyze", image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    edges = cv2.Canny(image, 100, 100)
    cv2.imshow("image", image)
    cv2.waitKey()
    cv2.destroyAllWindows()


def compareFrames(frame1, frame2):
    m = mse(frame1, frame2)
    s = ssim(frame1, frame2, multichannel=True)
    print("m: " + str(m))
    print("s: " + str(s))
    # need to include a threshold value in order to properly filter images


def mse(imageA, imageB):
    # Mean Squared Error - the lower the error, the more similar the images are
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err


def createSheetMusic():
    print("Create Sheet Music")


def destroyStoredFrames():
    print("Destroying stored frames now that PDF has been created.")
    shutil.rmtree('data')
