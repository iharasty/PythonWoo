'''
Created on Mar 23, 2020

@author: Isaac Harasty
tes
tes

'''

inputfile = open("testing.txt",mode = 'r',encoding = 'utf-8')
targetfile = open("testing2.txt", mode = 'w')

'''
code for moving inputfile information to targetfile without
its new lines
'''
for line in inputfile:
    for char in line:
        if char == "\n":
            print(line)
        else:
            targetfile.write(char)
    
    
    
inputfile.close()
targetfile.close()