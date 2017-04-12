import subprocess as cmd

def login_data(server) :

    if server == "store":
        # run teamUP
        cmd.check_output("adb shell am start -n com.estsoft.teamup/com.estsoft.teamup.ui.login.LoginActivity",
                         stderr=cmd.STDOUT, shell=True)
    elif server == "trial" :
        cmd.check_output("adb shell am start -n com.estsoft.teamuptest/com.estsoft.teamup.ui.login.TestLoginActivity",
                         stderr=cmd.STDOUT, shell=True)

    elif server == "cmcnu":
        cmd.check_output("adb shell am start -n com.estsoft.teamup.cmcnu/com.estsoft.teamup.ui.login.CmcnuLoginActivity",
                         stderr=cmd.STDOUT, shell=True)

def time_check():
    #cmd.check_output("adb shell input text jeongkuk@estsoft.com",
    #                     stderr=cmd.STDOUT, shell=True)
    #cmd.check_output("adb shell input keyevent KEYCODE_TAB",
    #                 stderr=cmd.STDOUT, shell=True)
    cmd.check_output("adb shell input text 비밀번호",
                     stderr=cmd.STDOUT, shell=True)
    cmd.check_output("adb shell input keyevent KEYCODE_TAB",
                     stderr=cmd.STDOUT, shell=True)
    cmd.check_output("adb shell input keyevent KEYCODE_ENTER",
                     stderr=cmd.STDOUT, shell=True)



if __name__ == "__main__":
    #login_data("store")
    #login_data("trial")
    #login_data("cmcnu")
    time_check()