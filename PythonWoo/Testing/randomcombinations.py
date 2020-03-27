import random 
class combo:
    def __init__(self, r1,r2):
        self.param1 = r1
        self.param2 = r2
    
    def getCombo(self):
        return (self.param1,self.param2)
    
print("change for git testing")
    
class comboCollection:
    def __init__(self):
        self.list = []
        self.count = 0
    
    def populate(self,num):
        for i in range(0,num):
            c = combo(0,0)
            c.param1 = random.randrange(0,100)
            c.param2 = random.randrange(0,100)
            self.list.append(c)
            self.count += 1
    
    def getCount(self):
        return self.count

comboList = comboCollection()
comboList.populate(5)
comboList.populate(5)
comboList.populate(5)
for i in range(0,comboList.getCount()):
    print(comboList.list[i].getCombo())


    

    