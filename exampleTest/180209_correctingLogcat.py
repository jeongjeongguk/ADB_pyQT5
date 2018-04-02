import subprocess, os

if __name__ == "__main__" :
    # print(os.getcwd())
    # '''
    # with open("foo.txt", "w") as f:
    # f.write("Life is too short, you need python")
    # '''
    with open("log_test.txt", "w") as f:
        f.write(
            # subprocess.check_output("adb shell logcat -d ", stderr=subprocess.STDOUT, shell=True).decode("utf-8")
            subprocess.check_call("adb shell logcat -d ", stderr=subprocess.STDOUT, shell=True).decode("utf-8")
            # str(os.system("adb shell logcat -d "))
        )

