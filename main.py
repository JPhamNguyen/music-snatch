import process_video
import sys
import os
from pytube import YouTube

if __name__ == '__main__':
    # print("Executing driver function")
    assert len(sys.argv) == 2, "First argument should be the YouTube link containing the music " \
                               "video with the embedded music sheets"
    video = YouTube(sys.argv[1])

    print(video.title)
    # filter for a stream with the highest quality possible for
    stream = video.streams.filter(res='1080p', mime_type='video/mp4').first()
    print(stream)


    # check for existing directories for storing files + images
    print(os.getcwd())

    if not os.path.exists(os.path.join(os.getcwd(), 'stored_files')):
        print("create a new directory to store YouTube videos + files")
        os.mkdir('stored_files')

    stream.download('stored_files')
