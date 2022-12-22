from moviepy import editor
from moviepy.video.io.VideoFileClip import VideoFileClip
import os.path as op
import glob
from moviepy.config import change_settings

class createVideo():
	def __init__(self):
		change_settings({"IMAGEMAGICK_BINARY": r"D:/PRO/ImageMagick/ImageMagick-7.1.0-Q16-HDRI/magick.exe"})
		self.file_path = glob.glob("./*.mp4")[0]

	def extractVideo(self):
		from_t =1384
		to_t = 1493
		video = VideoFileClip(self.file_path)
		annotated_clips = video.subclip(from_t, to_t)
		annotated_clips.write_videofile("movie_clip.mp4")

main = createVideo()
main.extractVideo()
