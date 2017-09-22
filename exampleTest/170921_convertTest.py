import imageio
import os, sys

class TargetFormat(object):
    GIF = ".gif"
    MP4 = ".mp4"
    AVI = ".avi"

def convertFile(inputpath, targetFormat):
    """Reference: http://imageio.readthedocs.io/en/latest/examples.html#convert-a-movie"""
    outputpath = os.path.splitext(inputpath)[0] + targetFormat
    print("converting\r\n\t{0}\r\nto\r\n\t{1}".format(inputpath, outputpath))

    reader = imageio.get_reader(inputpath)
    fps = reader.get_meta_data()['fps']
    fps = 10
    # print(fps) # 33.12
    writer = imageio.get_writer(outputpath, fps=fps)
    # print(enumerate(reader)) # <enumerate object at 0x047234E0>
    for i,im in enumerate(reader):
        sys.stdout.write("\rframe {0}".format(i))
        sys.stdout.flush()
        writer.append_data(im)
    print("\r\nFinalizing...")
    writer.close()
    print("Done.")

convertFile(r"C:\Users\Jeongkuk\PycharmProjects\00_share_170818_ADBGUI\src\dist\170919\170919_143222_SM-G900K_5.0_API_21.mp4",
            TargetFormat.GIF)

# mp4 파일 : 103MB, 녹화시 명령어 : adb shell screenrecord --bit-rate 10000000 /mnt/sdcard/ADB_record/test.mp4
# 해당파일을 10fps로 gif변환시 25분정도 소요됨. gif용량은 1.3 GB로 나옴 ( 끊김은 거의 없이 부드러우나 용량이 너무큼)