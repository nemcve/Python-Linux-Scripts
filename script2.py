#!usr/bin/python3

# Python script for searching for files in Linux based on the user input                                                  
# Usage: python3 script2.py /etc passwd                                                                                                                                                                                                               

import os                                                                                                                  
import argparse                                                                                                                                                                                                                                       


parser = argparse.ArgumentParser(description="Reading your input..")                                                       
parser.add_argument("pathsearch", help="Enter path name to search into: ")                                                 
parser.add_argument("filesearch", help="Enter filename to search for: ")                                                   
args = parser.parse_args()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  


for dirname, pathname, filename in os.walk(args.pathsearch):                                                                   
    for file in filename:                                                                                                          
        if file == args.filesearch:                                                                                                  
            print(os.path.join(dirname,file)) 
