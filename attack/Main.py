import reverse as r
import change_manifest as cm
import move_file as mv
import os

malware_apk = "/media/rivka/48C4E214C4E203D2/malware/all_app"
apks=os.listdir(malware_apk)
# r.key()
directory2 = "/media/rivka/48C4E214C4E203D2/malware/all_app_test"
index = 0
for i in apks:
   index +=1
   print(index)
   path = malware_apk + "/" + i
   r.depackaing_apk(path)
   path_open_apk = "/media/rivka/48C4E214C4E203D2/malware/change_file/" + i[: len(i)-4]
   check = mv.move_dir(path_open_apk)
   if check == 1:
      cm.change(path_open_apk)
      r.repacking_apk(path_open_apk)
      path_open_apk_after_change = path_open_apk + "/dist/{}".format(i[: len(i)-4])
      r.jarsigner(path_open_apk_after_change)
      r.zipalign(path_open_apk_after_change)
      directory1 = path_open_apk_after_change + "_mal.apk"
      cmd = "cp -r {} {}".format(directory1,directory2)
      os.system(cmd)


