# imageio.core.fetching.Need DownloadError: Need ffmpeg exe. You can download it by calling:
# 아래 두줄 실행해서, ffmpeg 다운로드실행
# import imageio
# imageio.plugins.ffmpeg.download()
# File saved as C:\Users\Jeongkuk\AppData\Local\imageio\ffmpeg\ffmpeg.win32.exe.

from moviepy.editor import *
# import os, sys
# currentPaths = os.getcwd()
# print(currentPaths)
# clip = (VideoFileClip("movie_360p.mp4")
#         .subclip((40.0),(50.0))
#         .resize(0.3)
#         )
clip = VideoFileClip("movie_360p.mp4")
clip.write_gif("movie_360p.gif") # 10시 49분 시작 52분에 40%까지 진행됨 / 1MB기준(103MB짜리를 줄인거)으로, 약 10분소요됨. -> 690MB로 늘어남
# 27.1MB mp4파일. resize(0.3)만 추가함. 10시 26분 시작 / 10시 35분 : 0% (2730/4626901) : 너무느림. 생성유무 확인위해 계속진행.
# 10시 44분 : 0%(4720/4626901) : 사용못할수준으로 느림.
# 11시 20분 : 이제 1% (40초~50초로 10초간만하는거. 51초 전체는 아직도 0%)