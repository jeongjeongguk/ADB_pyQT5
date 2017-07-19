if __name__ == "__main__":
    import wmi

    c = wmi.WMI()
    serviceToStart = 'Administrator'  # example
    for service in c.Win32_Service(Name=serviceToStart):
        service.StartService()

    import win32api,os

    # Company
    # win32api.ShellExecute(0,  # parent window
    #                       "runas",  # need this to force UAC to act
    #                       "C:\\Python35-32\\python3.exe "+os.getcwd()+"\\main.py",
    #                       None,
    #                       "C:\\Python35-32",  # base dir
    #                       1)  # window visibility - 1: visible, 0: background

    # Home
    win32api.ShellExecute(0,  # parent window
                          "runas",  # need this to force UAC to act
                          # "E:\Program Files (x86)\Python35-32\\python.exe {}\\main.py".format(os.getcwd()),
                          "notepad.exe",
                          None,
                          "notepad.exe",  # base dir
                          0)  # window visibility - 1: visible, 0: background