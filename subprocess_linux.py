#!usr/bin/python3

# Using a subprocess module to run an external linux command, "find", to find all the files with the extension .conf in the /etc folder

import subprocess

commands = ['powershell', '--command', 'dir']
s1 = subprocess.call(commands, shell=True)
