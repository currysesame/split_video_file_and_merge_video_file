
from moviepy import editor
from moviepy.video.io.VideoFileClip import VideoFileClip
import os.path as op
import glob
from moviepy.config import change_settings
# ref: https://python-climbing.com/moviepy-subtitle/

class createVideo():
    def __init__(self):
        change_settings({"IMAGEMAGICK_BINARY": r"D:/PRO/ImageMagick/ImageMagick-7.1.0-Q16-HDRI/magick.exe"})
        self.file_path = glob.glob("./*.mp4")#字幕を付けたい動画のパス

    def extractVideo(self):
        videos = []
        for videofile in self.file_path:
            video = VideoFileClip(videofile)
            videos.append(video)
        final_clip = editor.concatenate_videoclips(videos)
        final_clip.write_videofile("merged_video.mp4")

main = createVideo()
main.extractVideo()
