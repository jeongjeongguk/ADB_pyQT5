import ctypes
try:
    for num in range(0, 2):
        print(num)
        if True:
            if False:
                title = "설치 시작확인"
                version = "삭제후 설치"
                message = "버전 : {}\n".format(version)
            else:
                if True:
                    title = "덮어쓰기설치 시작확인"
                    message = "덮어쓰기"
                else:
                    print("덮어쓰기 연결된 기기 없음")
            # message = "message"
            # title = "title"
            userChoice = ctypes.windll.user32.MessageBoxW (0, "message : {}".format(message), title, 1)

            if userChoice == 1:
                if True:
                    print("삭제후 설치완료 : {}".format(num))
                else:
                    print("연결된 기기없음")
            else:
                print("설치취소")
        else:
            print("fileCheck Else")
except:
    print("Except")