try:
    import sys
    from pyadb import ADB
except ImportError as e:
    # should never be reached
    print("[f] Required module missing. %s" % e.args[0])
    sys.exit(-1)

ADB_PATH = "adb"

def main():
    # creates the ADB object
    adb = ADB()
    # IMPORTANT: You should supply the absolute path to ADB binary
    if adb.set_adb_path(ADB_PATH) is True:
        print("Version: %s" % adb.get_target_device() )
    else:
        print("Check ADB binary path")
    print(adb.__adb_path)

if __name__ == "__main__":
    main()