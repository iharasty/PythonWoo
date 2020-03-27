'''
Created on Mar 23, 2020

@author: Isaac
To add a target file to the glossary of old ProjectEuler answers
'''

from datetime import date
from idlelib.iomenu import encoding

targetfile = input("Please input the target file name...\n (no .py needed)\t")
header = input("Please input the header for the file...\n")
comments = input("Please enter any comments you would like to enter...\n")

'''
bufferstring = "-------------------"
header = bufferstring + header + bufferstring
'''

headerlength = (40.0 - len(header)) / 2.0
bufferstring = ""
for i in range (0,int(headerlength)):
    bufferstring = bufferstring + "-"


header = bufferstring + header + bufferstring
today = date.today()
linetwo = "\tLast edited: " + str(today)

if len(comments) != 0:
    comments = "\t~~~~~~~~~\n\n\t" + comments + "\n\n\t~~~~~~~~~"
else:
    comments = "~~~~~~~~~no comments~~~~~~~~~"

header = header + "\n" + linetwo + "\n" + comments
f = "OldProjectEuler.txt"
targetfile = targetfile + ".py"

currentfile = open(targetfile,mode='r',encoding='utf-8')
writefile = open("OldProjectEuler.txt",mode = 'a',encoding='utf-8')

writefile.write(header)
writefile.write("\n\n\n")

for line in currentfile:
    writefile.write(line)
    
    
writefile.write("\n\n\n")
print("Writing of " + str(targetfile) + " recorded to OldProjectEuler.txt")

writefile.close()
currentfile.close()