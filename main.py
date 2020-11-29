import process_video
import sys
import os


if __name__ == '__main__':
    # print("Executing driver function")
    assert len(sys.argv) == 2, "First argument should be the YouTube link containing the music " \
                               "video with the embedded music sheets"
    video = process_video.store_video(sys.argv[1])
    print("Current program has ended")
