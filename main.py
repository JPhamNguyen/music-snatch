import process_video
import sys
import os


if __name__ == '__main__':
    assert len(sys.argv) == 2, "First argument should be the YouTube link containing the music " \
                               "video with the embedded music sheets"
    # Download the video into a directory
    video = process_video.store_video(sys.argv[1])

    path_of_file = os.path.exists(os.path.join(os.getcwd(), 'stored_files'))
    print(path_of_file)
    process_video.frame_capture(path_of_file)

    # after video has been processed, store the pdf into another directory

