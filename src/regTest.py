#Python3 version of hugo24's snippet

# https://stackoverflow.com/questions/15128225/python-script-to-read-and-write-a-path-to-registry
import winreg

REG_PATH = r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"


# HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment
def set_reg(name, value):
    try:
        winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH, 0,
                                      winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False

def get_reg(name):
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH, 0,
                                      winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None

#Example MouseSensitivity
#Read value 
# print (get_reg('Path'))
# back_up = get_reg('Path')
# back_up =back_up.replace(";","\r\n")
# print(back_up)

#Set Value 1/20 (will just write the value to reg, the changed mouse val requires a win re-log to apply*)
#*For instant apply of SystemParameters like the mouse speed on-write, you can use win32gui/SPI
#http://docs.activestate.com/activepython/3.4/pywin32/win32gui__SystemParametersInfo_meth.html

# ======== [환경변수 상태조회] =======
# import os
# addPath = os.getcwd()
# set_reg('Path', addPath)
# print("============")
# print (get_reg('Path'))
# print("[복구]====")
# back_up = r"C:\ProgramData\Oracle\Java\javapath;C:\Python27\;C:\Python27\Scripts;C:\Python35-32\Lib\site-packages\PyQt5;C:\Python35-32\Scripts\;C:\Python35-32\;C:\Program Files (x86)\NVIDIA Corporation\PhysX\Common;%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\;C:\Program Files\Google\Google Apps Sync\;C:\Program Files\Google\Google Apps Migration\;C:\Users\Jeongkuk\AppData\Local\Android\sdk\platform-tools;C:\Users\Jeongkuk\AppData\Local\Android\sdk\tools;C:\Users\Jeongkuk\AppData\Local\Android\sdk\build-tools\24.0.1;C:\Users\Jeongkuk\AppData\Local\Android\sdk;C:\Program Files\Git\cmd;C:\MinGW\bin;C:\Python\Python35;C:\Python\Python35\Scripts;C:\Python\Python35\Lib\site-packages\PyQt5;C:\Program Files\Python35\Lib\site-packages\PyInstaller;C:\Program Files\Python35\Lib\site-packages\PyQt5\Qt\bin;C:\Program Files (x86)\Windows Kits\10\Redist\ucrt\DLLs\arm;C:\Program Files (x86)\Windows Kits\10\Redist\ucrt\DLLs\x86;C:\Program Files\Java\jdk1.7.0_79\bin;C:\Program Files\Java\jdk1.7.0_79;D:\sdk\android-sdk-windows;D:\sdk\android-sdk-windows\platform-tools;D:\sdk\android-sdk-windows\tools;C:\Program Files (x86)\QuickTime\QTSystem\;C:\Python35-32;C:\Program Files\nodejs\;C:\Program Files (x86)\Appium;C:\Program Files (x86)\Appium\node_modules;C:\Program Files\TortoiseGit\bin;C:\Program Files\PuTTY\;C:\Users\Jeongkuk\Downloads\geckodriver-v0.16.1-win64"
# set_reg('Path', back_up)
# print (get_reg('Path'))

# ======== [OS비트수 상태조회] =======
# REG_PATH = r"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
#  HKEY_LOCAL_MACHINE 아래에서 조회하므로, 제외하면 잘됨
REG_PATH = r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
print(get_reg("PROCESSOR_ARCHITECTURE"))