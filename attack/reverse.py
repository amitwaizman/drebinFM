import os


def depackaing_apk(name_apk):
    cmd = "apktool d {}".format(name_apk)
    os.system(cmd)

def repacking_apk(name_apk):
    cmd = "apktool b {}".format(name_apk)
    os.system(cmd)

def key():
    cmd = "keytool -alias bob -genkey -v -keystore mykey.keystore"
    os.system(cmd)

def jarsigner(name_apk):
    cmd = "echo 123456 | jarsigner -signedjar {}_1.apk -keystore mykey.keystore {}.apk bob".format(name_apk,name_apk)
    os.system(cmd)

def zipalign(name_apk):
    cmd = "zipalign -p -f -v 4 {}_1.apk {}_mal.apk".format(name_apk,name_apk)
    os.system(cmd)





