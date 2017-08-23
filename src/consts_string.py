from enum import Enum
class show_flag(Enum):
    foreground= 0x00001000
    # https://msdn.microsoft.com/en-us/library/ms645505(VS.85).aspx
    # MB_SETFOREGROUND 0x00010000L
    # The message box becomes the foreground window. Internally, the system calls the SetForegroundWindow function for the message box.
