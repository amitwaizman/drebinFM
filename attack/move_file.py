
import os

def move_dir(path):
    # files=os.listdir(path)
    # print(files)
    # for f in files:
        directory1= "android"
        # directory2 = ""
        path_dir = path + "/" + "smali"
        if "android" not in os.listdir(path_dir):
           directory2= path_dir
        elif "support" not in os.listdir(path_dir + "/android"):
            directory2= path_dir + "/android"
            directory1+= "/support"
        elif "v4" not in os.listdir(path_dir + "/android/support"):
            directory2= path_dir + "/android/support"
            directory1+= "/support/v4"
        elif "net" not in os.listdir(path_dir + "/android/support/v4"):
            directory2= path_dir + "/android/support/v4"
            directory1+= "/support/v4/net"
        else:
            print("not exist")
            return -1
        cmd = "cp -r {} {}".format(directory1,directory2)
        os.system(cmd)
        return 1