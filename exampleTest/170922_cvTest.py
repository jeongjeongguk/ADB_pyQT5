import cv2
file_path = "./movie_360p.mp4"  #change to your own video path
vid = VideoCapture( file_path )
height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)