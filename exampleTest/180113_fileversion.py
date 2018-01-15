from win32api import GetFileVersionInfo, LOWORD, HIWORD
import os


x64_programfiles = "C:\\Program Files (x86)\\"
PROGRAMFILES = os.getenv('programfiles') +"\\"
PROGRAMDATA = os.getenv('programdata') +"\\"
APPDATA = os.getenv('appdata') + "\\"
ALUPDATE = "ESTsoft\\ALUpdate\\"
ALAUTH = "ESTsoft\\ALAUTH\\"
ALCM = "ESTsoft\\ALCM\\"
ESTSOFT = "ESTsoft\\"

CONFIRM_LIST_ALUPDATE = [
    ["AZMain.dll",""],
    ["ALUpdate.exe",""],
    ["ALUpdateEx.dll",""],
    ["ALUpExt.exe",""],
    ["ALUpProduct.exe",""],
    ["eausvc.exe",""],
    ["ko-KR.dll",""],
    ["unins000.exe",""],
    ["ezt.exe",""],
    ["ALAd.dll",""]
]

PROGRAMLIST = [
    "ALCapture\\",
    "ALDrive\\",
    "ALKeeper\\",
    "ALPDF\\",
    "ALSee\\",
    "ALSong\\",
    "ALToolBar\\",
    "ALZip\\"
]

CONFIRM_LIST_PROGRAMLIST = [
    ["ALUpdate.dll ",""],
    ["ALCMProxy.dll",""],
    ["ALSTS.dll",""]
]
AUTHSERIAL_DLL = [["AuthSerial.dll",""]]

def get_version_number(filename):
    try:
        info = GetFileVersionInfo(filename, "\\")
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        return HIWORD(ms), LOWORD(ms), HIWORD(ls), LOWORD(ls)
    except:
        return "None"

if __name__ == "__main__":
    # ==================================================================================================================
    print("="*5 + "[ {} ]".format(PROGRAMFILES + ALUPDATE) + "="*5)
    for i in range(0,len(CONFIRM_LIST_ALUPDATE)):
        try :
            CONFIRM_LIST_ALUPDATE[i][1] = ".".join([str(i) for i in get_version_number(
            "{}".format(PROGRAMFILES + ALUPDATE + CONFIRM_LIST_ALUPDATE[i][0]))])
        except :
            CONFIRM_LIST_ALUPDATE[i][1] = "None"
        print("{} : ".format(CONFIRM_LIST_ALUPDATE[i][0]) + CONFIRM_LIST_ALUPDATE[i][1])
    # ==================================================================================================================
    print("="*5 + "[ {} ]".format(APPDATA + ALAUTH) + "="*5)
    try :
        AuthReg_exe = ".".join([str(i) for i in get_version_number(
            "{}".format( APPDATA + ALAUTH + "AuthReg.exe"))])
    except :
        AuthReg_exe = "None"
    print("AuthReg.exe : " + AuthReg_exe)
    # ==================================================================================================================
    print("="*5 + "[ {} ]".format(PROGRAMDATA + ALCM) + "="*5)
    try :
        ALCMUpdate_exe = ".".join([str(i) for i in get_version_number(
            "{}".format( PROGRAMDATA + ALCM + "ALCMUpdate.exe"))])
    except :
        ALCMUpdate_exe = "None"
    print("{} :   {}".format("ALCMUpdate.exe", ALCMUpdate_exe))
    # ==================================================================================================================
    for i in range(0, len(PROGRAMLIST)):
        if os.path.isdir("{}".format(PROGRAMFILES + ESTSOFT + PROGRAMLIST[i])) :
            print("=" * 5 + "[ {} ]".format(PROGRAMFILES + ESTSOFT + PROGRAMLIST[i]) + "=" * 5)
            for i in range(0, len(CONFIRM_LIST_PROGRAMLIST)):
                try:
                    CONFIRM_LIST_PROGRAMLIST[i][1] = ".".join([str(i) for i in get_version_number(
                        "{}".format(PROGRAMFILES + ESTSOFT + PROGRAMLIST[i] + CONFIRM_LIST_PROGRAMLIST[i][0]))])
                except:
                    CONFIRM_LIST_PROGRAMLIST[i][1] = "None"
                if CONFIRM_LIST_PROGRAMLIST[i][1] != "N.o.n.e":
                    print("{} :   {}".format(CONFIRM_LIST_PROGRAMLIST[i][0],CONFIRM_LIST_PROGRAMLIST[i][1]))
        else :
            print("=" * 5 + "[ {} ]".format(PROGRAMFILES + ESTSOFT + PROGRAMLIST[i]) + "=" * 5)
            print(PROGRAMLIST[i] + "'s foleder isn't Exist")
    # ==================================================================================================================
    # for i in range(0, len(PROGRAMLIST)):
    #     if os.path.isdir("{}".format(APPDATA + ESTSOFT + PROGRAMLIST[i])) :
    #         print("=" * 5 + "[ {} ]".format(APPDATA + ESTSOFT + PROGRAMLIST[i]) + "=" * 5)
    #         for i in range(0, len(PROGRAMLIST)):
    #             # print("{}".format(APPDATA + ESTSOFT + PROGRAMLIST[i] + AUTHSERIAL_DLL[i][0]))
    #             if os.path.isfile("{}".format(APPDATA + ESTSOFT + PROGRAMLIST[i] + AUTHSERIAL_DLL[i][0])) :
    #                 print("=" * 5 + "[ {} ]".format(APPDATA + ESTSOFT + PROGRAMLIST[i]) + "=" * 5)
    #             else :
    #                 print("{}".format(APPDATA + ESTSOFT + PROGRAMLIST[i]) + "=" * 5)
    #             try:
    #                 # AUTHSERIAL_DLL[i][1] = ".".join([str(i) for i in get_version_number(
    #                 #     "{}".format(APPDATA + ESTSOFT + PROGRAMLIST[i] + AUTHSERIAL_DLL[i][0]))])
    #                 pass
    #             except:
    #                 pass
    #             # if AUTHSERIAL_DLL[i][1] != "N.o.n.e":
    #             #     print("{} :   {}".format(AUTHSERIAL_DLL[i][0],AUTHSERIAL_DLL[i][1]))
    #     else :
    #         print("=" * 5 + "[ {} ]".format(APPDATA + ESTSOFT + PROGRAMLIST[i]) + "=" * 5)
    #         print(PROGRAMLIST[i] + "'s foleder isn't Exist")
    # ==================================================================================================================

    os.system("pause")
