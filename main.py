import process_video
import sys
import os


if __name__ == '__main__':
    assert len(sys.argv) == 2, "First argument should be the YouTube link containing the music " \
                               "video with the embedded music sheets"
    # Download the video into a directory + return file name
    file_name = process_video.store_video(sys.argv[1])
    video = file_name + ".mp4"
    print(type(video))
    process_video.frame_capture(video)

