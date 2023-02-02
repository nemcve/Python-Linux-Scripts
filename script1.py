#!/usr/bin/env/ python3


# script that lists all files in a directory, including all files 
# in subfolders of that directory


import os

dirs_files = list(os.path.walk("/home/Nemanja"))

for dirname, pathname, filename in dirs_files:
    print(dirname)
    for file in filename:
        print(os.path.join(dirname,file))
