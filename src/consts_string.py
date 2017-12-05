from enum import Enum
class show_flag(Enum):
    foreground= 0x00001000
    MB_OK = 0x0
    MB_OKCXL = 0x01
    MB_YESNOCXL = 0x03
    MB_YESNO = 0x04
    MB_HELP = 0x4000
    ICON_EXLAIM = 0x30
    ICON_INFO = 0x40
    ICON_STOP = 0x10
    # https://msdn.microsoft.com/en-us/library/ms645505(VS.85).aspx
    # MB_SETFOREGROUND 0x00010000L
    # The message box becomes the foreground window. Internally, the system calls the SetForegroundWindow function for the message box.


class alyac(Enum):
    run = ""
    약관동의 = "com.estsoft.alyac.user_interface.pages.SubPageActivity"
    home = "com.estsoft.alyac.user_interface.MainActivity"
    detect = ""
    사용자이용약관동의 = "com.estsoft.alyac:id/checkbox_usage_outbox"
    사용자이용약관동의_다음 = "com.estsoft.alyac:id/button_next"
    권한안내_다음 = "com.estsoft.alyac:id/button_next"
    와이파이3G사용 = "com.estsoft.alyac:id/radio_button_wifi_and_3g_outbox"
    와이파이만 = "com.estsoft.alyac:id/radio_button_wifi_only_outbox"
    권한안내_완료 = "com.estsoft.alyac:id/button_next"

    홈_코치마크_시작하기 =  "com.estsoft.alyac:id/bottom_button_area"
    # 홈_검사하기 = "com.estsoft.alyac:id/text_view_main_scan_button_message"
    홈_검사하기 = "text_view_main_scan_button_message"
    start = ""
    pause = ""
    update = ""

if __name__ == "__main__":
    print(show_flag.test)
    # alyac = alyac()
    print(alyac.홈_검사하기)