import os
import moviepy
import subprocess as cmd
import win32com.shell.shell as win32shell
import re

# os.system("ffmpeg -i resize.mp4") #OK> ffmpeg 폴더를 path에 추가.
# # Stream #0:0(eng): Video: h264 (Baseline) (avc1 / 0x31637661), yuv420p, 1080x1920, 9910 kb/s, 33.12 fps, 90k tbr, 90k tbn, 180k tbc (default)
#
# # os.system("ffmpeg -i resize.mp4 -vf scale=640:-1 movie_360p.mp4") #OK> ffmpeg 폴더를 path에 추가. 스케일조절로, 용량줄임.
# os.system("ffmpeg -i movie_360p.mp4") #OK> ffmpeg 폴더를 path에 추가.
# # Stream #0:0(eng): Video: h264 (High) (avc1 / 0x31637661), yuv420p, 640x1138, 395 kb/s, 33.12 fps, 33.12 tbr, 2403k tbn, 66.24 tbc (default)
#
# # C:\Users\Jeongkuk\PycharmProjects\00_share_170818_ADBGUI\src\dist\170922
# paths = r"C:\Users\Jeongkuk\PycharmProjects\00_share_170818_ADBGUI\src\dist\170922"
# os.system(r"ffmpeg -i {}\170922_164922_SM-G900K_5.0_API_21.mp4".format(paths)) #OK> ffmpeg 폴더를 path에 추가.
# # Stream #0:0(eng): Video: h264 (Baseline) (avc1 / 0x31637661), yuv420p, 1080x1920, 8272 kb/s, 48.63 fps, 90k tbr, 90k tbn, 180k tbc (default)
# # s5 5.0 기준


from moviepy.editor import *
# clip = VideoFileClip('movie_360p.mp4')
# imsi = r'C:\Users\Jeongkuk\PycharmProjects\androidADB\screenshot\1012_1450_08_Nexus6P_8.0.0_API26.mp4'
# imsi = r'C:\Users\Jeongkuk\Documents\AireCam\1012_1450_08_Nexus6P_8.0.0_API26.mp4'
# imsi = r'C:\Users\Jeongkuk\PycharmProjects\androidADB\exampleTest\iphone5s_10.2.1.mov'
# clip = VideoFileClip(imsi)
# org_size = clip.aspect_ratio
# print(org_size)
# print(clip.size)
# # print(clip.reader.size)  # 영상사이즈 줄일때도, 기존의 영상 사이즈를 가지고 온다음에, 그 비율에 맞춰서 조율하는게 나을지 확인필요.
# # print(org_size)
# #
# # import cv2
# # file_path = "./movie_360p.mp4"  #change to your own video path
# # vid = VideoCapture( file_path )
# # height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
# # width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
#

# lib써서(VideoFileClip) 프레임 사이즈 정보확인
# imsi = r'C:\Users\Jeongkuk\PycharmProjects\androidADB\exampleTest\iphone5s_10.2.1.mov'
# clip = VideoFileClip(imsi)
# org_width, org_height = clip.size[0], clip.size[1]
# print(org_width); print(org_height)

# 영상 프레임크기축소하여, gif 변환
# imsi = r'C:\Users\Jeongkuk\PycharmProjects\androidADB\exampleTest\iphone5s_10.2.1.mov'
# org_width = cmd.check_output("ffprobe -v error -of flat=s=_ -select_streams v:0 -show_entries stream=width {}".format(imsi)).decode("utf-8")
# org_width = re.sub('\s', '', org_width)
# org_width = int(org_width.split("=")[1])
# org_height = cmd.check_output("ffprobe -v error -of flat=s=_ -select_streams v:0 -show_entries stream=height {}".format(imsi)).decode("utf-8")
# org_height = re.sub('\s', '', org_height)
# org_height = int(org_height.split("=")[1])
# downPercent = 0.5
# tmp_width, tmp_height = int(org_width * downPercent), int(org_height * downPercent)
# os.system("ffmpeg -i {} -pix_fmt rgb24 -r 10 -s {}x{} downSize_3.gif".format(imsi, tmp_width, tmp_height)) #Invalid frame size:

# 영상크기축소없이, gif 변환
# imsi = r'C:\Users\Jeongkuk\PycharmProjects\androidADB\src\dist\171108\171108\171108_140525_SM-G930K_7.0_API_24.mp4'
imsi = r'C:\Users\Jeongkuk\Desktop\title.mov'
os.system("ffmpeg -i {} -pix_fmt rgb24 -r 10 recording.gif".format(imsi)) #OK> ffmpeg 폴더를 path에 추가.

# 영상 자르기
# ffmpeg   -i   동영상.avi -ss  600  -t  120  -vcodec copy -acodec copy  clip.avi
# 출처: http://crynut84.tistory.com/6 [Life is Dynamic]
# imsi = r'C:\Users\Jeongkuk\PycharmProjects\androidADB\exampleTest\iphone7_11.0.mov'
# imsi = r'C:\Users\Jeongkuk\PycharmProjects\androidADB\src\171114\171114\171114\171114_154651_SM-G925S_6.0.1_API_23.mp4'
# imsi = r'C:\Users\Jeongkuk\Desktop\recording.mp4'
# startTime = "90" #second. cutting start time.
# ToCutTime = "20" #second. cutting during time from start time.
# os.system("ffmpeg -i {} -ss {} -t {} -vcodec copy -acodec copy clip.mp4".format(imsi, startTime, ToCutTime))
#TODO : 영상이 150초가량 되는 원본에서, 90초부분부터 110초까지 뽑아낼려는데 못 뽑아냄.

# File 'movie_360p_320_tmp.gif' already exists. Overwrite ? [y/N]
#
# # import moviepy.editor as mp
# # clip = mp.VideoFileClip("resize.mp4")
# # clip_resized = clip.resize(height=360) # make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
# # clip_resized.write_videofile("movie_resized.mp4")