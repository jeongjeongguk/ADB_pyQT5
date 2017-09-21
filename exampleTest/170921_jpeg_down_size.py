from PIL import Image

file = r'C:\Users\Jeongkuk\PycharmProjects\00_share_170818_ADBGUI\src\dist\170920\original.jpg'
New_file = r'C:\Users\Jeongkuk\PycharmProjects\00_share_170818_ADBGUI\src\dist\170920\test4.jpg'

img = Image.open(file)
downPer = 0.25
resize = (int(img.width * downPer),int(img.height * downPer))
print(resize)
img = img.resize(resize)
img.save(New_file, 'jpeg', quality=85)
print(img.width)
print(img.height)
import os
print(os.getcwd())