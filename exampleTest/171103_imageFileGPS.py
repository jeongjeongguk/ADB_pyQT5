from PIL import Image  # PIL 모듈 사용
from PIL.ExifTags import TAGS  # PIL 모듈 사용
import folium  # folium 모듈 사용
import logging

filename = input('Input your Image File name : ')  # ‘ filename ‘이란 변수에 파일 이름을 받음
extension = filename.split('.')[-1]  # split 이라는 함수사용 _ 문자열 나누기
if (extension == 'jpg') | (extension == 'JPG') | (extension == 'jpeg') | (extension == 'JPEG'):
    # 파일 확장자가 ‘ jpg ‘ , ‘ JPG ‘ , ‘ jpeg ‘ , ‘ JPEG ‘ 인지 확인
    try:  # 시도
        img = Image.open(filename)  # ‘ img ’ 라는 변수에서 ‘ filename ’ 을 열음
        info = img._getexif()
        exif = {}
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)  # 속성 불러옴
            exif[decoded] = value
        try:
            Camera_Maker = exif['Make']  # 카메라 모델을 ‘ Camear_Maker ’ 에 저장
            Camera_Model = exif['Model']  # 카메라 모델 이름을 ‘ Camera_Model ‘ 에 저장
            Camera_Software = exif['Software']  # 카메라 소프트웨어 버전을 ‘ Camera_Software ‘ 에 저장
            Camera_Date = exif['DateTimeOriginal']  # 사진찍은(만든)날짜를 ‘ Cameara_Date ‘ 에 저장

            print("\n---------Information Photo---------\n")
            print("- File name : " + filename + "\n")  # Filename 을 출력
            print("- Cameara Model : " + Camera_Maker + "\n") # Camera Model 을 출력
            print("- Camera Model Name : " + Camera_Model + "\n")  # Camera Model Name 을출력
            print("- Cameara Software : " + Camera_Software + "\n")  # Camera Software 을 출력
            print("- Taking Photo Time : " + Camera_Date + "\n")  # Camear_Date 를 출력
        except:
            # logging.exception("message")
            print("- No Cammera's information. ")
            pass

        exifGPS = exif['GPSInfo']  # GPS 좌표값을 exifGPS에 저장
        # GPS 좌표 처리
        X_Data = exifGPS[2]
        Y_Data = exifGPS[4]
        X_Deg = X_Data[0][0] / float(X_Data[0][1])
        X_Min = X_Data[1][0] / float(X_Data[1][1])
        X_Sec = X_Data[2][0] / float(X_Data[2][1])
        Y_Deg = Y_Data[0][0] / float(Y_Data[0][1])
        Y_Min = Y_Data[1][0] / float(Y_Data[1][1])
        Y_Sec = Y_Data[2][0] / float(Y_Data[2][1])

        Lat = (X_Deg + (X_Min + X_Sec / 60.0) / 60.0)
        if exifGPS[1] == 'S': Lat = Lat * -1
        Lon = (Y_Deg + (Y_Min + Y_Sec / 60.0) / 60.0)
        if exifGPS[3] == 'W': Lon = Lon * -1
        X = Lat  # 경도를 X에 저장
        Y = Lon  # 위도를 Y에 저장
        map_osm = folium.Map(location=[X, Y], zoom_start=15)  # folium 모듈을 사용하여 좌표값을 지도에 찍음, zoom_start는 지도의 확대범위를 나타냄
        folium.Marker([X, Y], popup=filename).add_to(map_osm)  # 좌표에 마커를 찍음
        map_osm.save('Map_{}.html'.format(filename))  # 지도를 Map.html에 저장
        print("- Located GPS  " + str(Lat) + "," + str(Lon) + "\n")  # 좌표 출력
        print("- Check your dictectory Map_{}.html!!!")

    except:
        logging.exception("message")
        print("- No Located GPS. ")  # 좌표가 출력 되지 않음
        pass
