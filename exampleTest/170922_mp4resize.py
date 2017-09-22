import os
import moviepy
import subprocess as cmd
import win32com.shell.shell as win32shell

os.system("ffmpeg -i resize.mp4") #OK> ffmpeg 폴더를 path에 추가.
# Stream #0:0(eng): Video: h264 (Baseline) (avc1 / 0x31637661), yuv420p, 1080x1920, 9910 kb/s, 33.12 fps, 90k tbr, 90k tbn, 180k tbc (default)

# os.system("ffmpeg -i resize.mp4 -vf scale=640:-1 movie_360p.mp4") #OK> ffmpeg 폴더를 path에 추가.
os.system("ffmpeg -i movie_360p.mp4") #OK> ffmpeg 폴더를 path에 추가.
# Stream #0:0(eng): Video: h264 (High) (avc1 / 0x31637661), yuv420p, 640x1138, 395 kb/s, 33.12 fps, 33.12 tbr, 2403k tbn, 66.24 tbc (default)

# C:\Users\Jeongkuk\PycharmProjects\00_share_170818_ADBGUI\src\dist\170922
paths = r"C:\Users\Jeongkuk\PycharmProjects\00_share_170818_ADBGUI\src\dist\170922"
os.system(r"ffmpeg -i {}\170922_164922_SM-G900K_5.0_API_21.mp4".format(paths)) #OK> ffmpeg 폴더를 path에 추가.
# Stream #0:0(eng): Video: h264 (Baseline) (avc1 / 0x31637661), yuv420p, 1080x1920, 8272 kb/s, 48.63 fps, 90k tbr, 90k tbn, 180k tbc (default)
# s5 5.0 기준


# from moviepy.editor import *
# clip = VideoFileClip('movie_360p.mp4')
# org_size = clip.aspect_ratio
# # print(clip.reader.size)  # 영상사이즈 줄일때도, 기존의 영상 사이즈를 가지고 온다음에, 그 비율에 맞춰서 조율하는게 나을지 확인필요.
# # print(org_size)
# #
# # import cv2
# # file_path = "./movie_360p.mp4"  #change to your own video path
# # vid = VideoCapture( file_path )
# # height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
# # width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
#
# tmp_height = 320 * org_size
# tmp_height = int(tmp_height)
# # print(tmp_height)
# os.system("ffmpeg -i movie_360p.mp4 -pix_fmt rgb24 -r 10 -s {}x240 movie_360p_320_tmp.gif".format(tmp_height)) #OK> ffmpeg 폴더를 path에 추가.
#
# # import moviepy.editor as mp
# # clip = mp.VideoFileClip("resize.mp4")
# # clip_resized = clip.resize(height=360) # make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
# # clip_resized.write_videofile("movie_resized.mp4")