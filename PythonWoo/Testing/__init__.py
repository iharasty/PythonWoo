
'''def ispal(num1,num2):
    index = 0
    numstring = str(num1*num2)
    ispal = True
    while ispal and index < len(numstring) / 2:
        if numstring[index] != numstring[len(numstring) - index - 1]:
            ispal = False
        index += 1
    
    return ispal
'''
from _ast import If

"""def ispal(num):
    index = 0
    numstring = str(num)
    ispal = True
    while ispal and index < len(numstring) / 2:
        if numstring[index] != numstring[len(numstring) - index - 1]:
            ispal = False
        index += 1
    return ispal"""

num = 37498620
divisor = 2
found = False
while not found:
    print(num) 
    num += 10 
    while divisor != -1 and divisor < 21:
        #print(str(num) +    ": " + str(num % divisor))
        if num % divisor == 0:
            divisor += 1
        else:
            divisor = -1 
    
    if divisor == 21:
        found = True
    elif divisor == -1:
        divisor = 2
        
print(num)