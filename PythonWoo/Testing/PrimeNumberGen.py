'''
Created on Mar 30, 2020

@author: Isaac

Initialize this class to test if numbers are prime or not.

'''

setOfPrimes = {2,3,5,7,11}
currMax = 11

def genNextPrime(number):

    current = number
    divisible = False
    found = False
    
    while not found:
        
        testprimes = set(setOfPrimes)
        
        while not divisible and len(testprimes) != 0:
            
            if current % testprimes.pop() == 0:
                divisible = True
                
        if not divisible:
            return current
        else:
            divisible = False
            current += 1
    
            
    

def genPrimes(increment = len(setOfPrimes)):
    
    global currMax
    
    for i in range(0,increment):
        
        currMax = genNextPrime(currMax)
        setOfPrimes.add(currMax)
    
def isPrime(number):
    
    if number > currMax:
        genPrimes()
        return isPrime(number)
    
    if number < 2:
        return -1
    
    if not isinstance(number, int):
        raise TypeError('Needs type Int')
    
    return setOfPrimes.__contains__(number)

genPrimes(100)
