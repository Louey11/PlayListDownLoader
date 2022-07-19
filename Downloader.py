from dataclasses import replace
import sys # import sys 
from pytube import *


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining 
    percentage_of_completion = bytes_downloaded / total_size * 100
    print("{:.2f}".format(percentage_of_completion) ,"%") 
#"{:.2f}".


link = input('Please enter a url link\n')
PATH = input('Please Enter your out path\n')
PATH=PATH.replace('\\','\\\\')



yt = Playlist(link)

for video in yt.videos :
    print(f"the video title is : \n {video.title} \n -----Downloading Process----")
    video.register_on_progress_callback(on_progress)
    stream = video.streams.get_highest_resolution()
    finished = stream.download(output_path= PATH)
    print ('---------Download is complete------')

sys.exit()