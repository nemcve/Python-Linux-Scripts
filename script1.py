#!/usr/bin/env/ python3


# script that lists all files in a directory, including all files 
# in subfolders of that directory


import os


for dirname, pathname, filename in os.walk("/home/Nemanja"):
    print(dirname)
    for file in filename:
        print(os.path.join(dirname,file))

