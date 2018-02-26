from pywinauto.application import Application
import os

class defStr(object) :
    x64 = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\"
    x86 = ""
    sysinfo = x64 if os.path.exists("C:\\Program Files (x86)") else x86
    chorme_path = sysinfo + "chrome.exe"

    naver = "www.naver.com"
    daum = "www.daum.net"


class connectSite(object):
    def __init__(self, site):
        self._site = site

    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, site):
        self._site = site

    @classmethod
    def chkCap(self):
        app = Application().start(defStr.chorme_path + " " + defStr.naver)
        # app.type_keys(self._site, with_spaces = True)

if __name__ == "__main__" :
    connectSite(defStr.naver).chkCap()


