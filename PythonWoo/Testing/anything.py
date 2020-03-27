

file = open('testing.txt', mode = 'r')

def parseFile(file):
    
    masteremptylist = []
    char = file.read(2)
    
    while char != "":
        
        emptylist = []
        
        
        while char != '\n':
            
            if char == " ":
                char = file.read(2)
            else:
                num = int(char)
                emptylist.append(num)
                char = file.read(1)
        
        
        masteremptylist.append(emptylist)
        char = file.read(2)
        
    for i in range(0,len(masteremptylist)):
        masteremptylist[i] = tuple(masteremptylist[i])
        
    masteremptylist = tuple(masteremptylist)
    
    return masteremptylist
            
matrix = parseFile(file)

def maxhorizontals(matrix):
    
    maxsum = 0
    start = ()
    '''i = rows'''
    for i in range(0,len(matrix)):
        '''j = collumns'''
        for j in range(0,len(matrix[i]) - 4):
            '''k = 4 in a row'''
            sum = 1
            for k in range(0,4):
                sum *= matrix[i][j + k]
            
            if sum > maxsum:
                maxsum = sum
                start = (i , j)
                
    print("max = " + str(maxsum) + " starting " + str(start))

def maxrightdiagnals(matrix):
    
    maxsum = 0
    start = ()
    
    '''i = rows'''
    for i in range(0,len(matrix) - 4):
        '''j = collumns'''
        for j in range(0,len(matrix[i]) - 4):
            '''k = 4 in a row'''
            sum = 1
            for k in range(0,4):
                sum *= matrix[i + k][j + k]
            
            if sum > maxsum:
                maxsum = sum
                start = (i , j)
                
    print("max = " + str(maxsum) + " starting " + str(start))
    
def maxleftdiagnals(matrix):
    
    maxsum = 0
    start = ()
    
    '''i = rows'''
    for i in range(0,len(matrix) - 4):
        '''j = collumns'''
        for j in range(0,len(matrix[i]) - 4):
            '''k = 4 in a row'''
            sum = 1
            for k in range(0,4):
                sum *= matrix[i + k][j + (3 - k)]
            
            if sum > maxsum:
                maxsum = sum
                start = (i , j)
                
    print("max = " + str(maxsum) + " starting " + str(start))    

def maxverticals(matrix):
    
    maxsum = 0
    start = ()
    
    '''i = rows'''
    for i in range(0,len(matrix) - 4):
        '''j = collumns'''
        for j in range(0,len(matrix[i])):
            '''k = 4 in a row'''
            sum = 1
            for k in range(0,4):
                sum *= matrix[i + k][j]
            
            if sum > maxsum:
                maxsum = sum
                start = (i , j)
                
    print("max = " + str(maxsum) + " starting " + str(start))

print(matrix)
maxhorizontals(matrix)
maxverticals(matrix)
maxrightdiagnals(matrix)
maxleftdiagnals(matrix)