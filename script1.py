#!/usr/bin/python3


# Script that lists all files in a directory, including all files in subfolders of that directory
# Useful when used with grep
# Usage python3 script1.py | grep ".terraform"

import os
for dirname, pathname, filename in os.walk("/home/Nemanja"):
    print(dirname)
    for file in filename:
        print(os.path.join(dirname,file))

