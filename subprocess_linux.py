#!usr/bin/python3

# Using a subprocess module to run an external linux command, "find", to find all the files with the extension .conf in the /etc folder

import subprocess

commands = ['sudo', 'find', '/etc', '-name', '*.conf']
s1 = subprocess.Popen(commands, shell=False, stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE, universal_newlines=True)


out, err = s1.communicate()
rt = s1.wait()
print(out)
print(err)
