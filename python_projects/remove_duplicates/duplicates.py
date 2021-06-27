import filecmp
import os

files_list=os.listdir()
n=0
for pics in files_list:
    if pics==files_list[n]:
        if filecmp.cmp(files_list[n],pics):
            os.remove(pics)
            print("similar ")
            n+=1
        else:
            n+=1
            print("non similar ")







