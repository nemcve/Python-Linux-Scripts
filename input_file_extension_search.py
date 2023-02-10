# Search inside the directories and their subdirectories for the files with a specific extension
# Usage:
# Linux - python3 script3.py /home/Nemanja .txt | less
# Windows - python3 script3.py C:/Users/Nemanja .txt | out-host -paging

import os
import argparse

parser = argparse.ArgumentParser(description="Waiting for your input...")
parser.add_argument("pathsearch", help="Please enter a directory to search: ")
parser.add_argument("extensionfinder",
                    help="Please enter a file extension to search: ")
args = parser.parse_args()

for dirname, dirpath, filename in os.walk(args.pathsearch):
    for file in filename:
        if file.endswith(args.extensionfinder):
            print(os.path.join(dirname, file))
