'''
Created on Mar 25, 2020

@author: Isaac
'''

import json
from datetime import datetime,timedelta
from textwrap import indent


'''
printing out old JSONs from text file
'''

with open('jsonrecords.json','r') as f:
    importdata = json.load(f)

print("Printing previous access...")


for acc in importdata["entries"]:
    print("\t" + acc["access"])
    
print("\ntotal amount of access: " + str(len(importdata["entries"])))

now = datetime.now()

if len(importdata) != 0:
    lastentry = importdata["entries"][-1]
    lastentrystring = lastentry["access"]
    lastentrydatetime = datetime.fromisoformat(lastentrystring)
    print("last access was " + str(lastentrydatetime))
    print("time difference: " + str(now - lastentrydatetime))
    

newdata = { "access" : str(now) }

importdata["entries"].append(newdata)

with open('jsonrecords.json','w') as f:
    json.dump(importdata,f)

