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
    # blurred = cv2.GaussianBlur(image, (5, 5), 0)
    # thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.threshold(image, 60, 255, cv2.THRESH_BINARY)[1]

    contours = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    contours = imutils.grab_contours(contours)

    for c in contours:
        approx = cv2.approxPolyDP(c, 0.01 * cv2.arcLength(c, True), True)
        cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
        x = approx.ravel()[0]
        y = approx.ravel()[1] - 5
        if len(approx) == 3:
            cv2.putText(image, "Triangle", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
        elif len(approx) == 4:
            x1, y1, w, h = cv2.boundingRect(approx)
            aspect_ratio = float(w) / float(h)
            print(aspect_ratio)
            if 0.95 <= aspect_ratio <= 1.05:
                cv2.putText(image, "Square", (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)

    cv2.imshow("img", image)
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
