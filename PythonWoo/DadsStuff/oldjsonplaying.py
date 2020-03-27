'''
Created on Mar 25, 2020

@author: Isaac
'''

import json
from datetime import datetime

now = datetime.now()
data = { "a" : str(now) }

print(data["a"])
print(json.dumps(data))


'''
now = datetime.now()
print(now)
print(now.month)
print(datetime.fromisoformat('2011-11-11T06:00:00'))


testjson = {
    "entries":[
        {"access":str(now)}
        ]
}

print(testjson["entries"])
print(type(testjson["entries"][0]))

x = json.dumps(testjson, indent = 2)

print(x)
print(type(x))

now = datetime.now()

newobject = { "access": str(now) }

testjson["entries"].append(newobject)

print(json.dumps(testjson, indent = 2))
'''
