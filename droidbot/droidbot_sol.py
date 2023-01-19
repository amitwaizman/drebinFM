import os,random


def run_droid(inp,c,out):
        output_dir=out+"/"+c.split(".")[0]
        os.makedirs(output_dir, exist_ok=True)
        os.system("python3 start.py -a "+inp+os.path.sep+c+" -o "+output_dir+" -policy dfs_greedy -grant_perm -is_emulator -ignore_ad -keep_env -count 5 -timeout 300")

inp="/media/rivka/48C4E214C4E203D21/compare_apk/all_app"
out="/media/rivka/48C4E214C4E203D21/compare_apk/all_app_output"
for c in os.listdir(inp):#run files from input folder
        try:
                run_droid(inp,c,out)
                
        except:
                continue  
