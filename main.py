import process_video
import process_images
import sys
import os


if __name__ == '__main__':
    assert len(sys.argv) == 2, "First argument should be the YouTube link containing the music " \
                               "video with the embedded music sheets"
    # Download the video into a directory + return file name
    file_name = process_video.store_video(sys.argv[1])

    # filter for inputted file and use a method call
    video = file_name + ".mp4"

    # capture frames of video
    # process_video.frame_capture(video)

    # process and filter unnecessary images
    process_images.filterFrames(video)

    # destroy no longer needed files and frames
    # process_images.destroyStoredFrames()
