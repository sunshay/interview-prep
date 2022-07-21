import json
from tkinter import W
with open('congo.json') as file:
    data = json.load(file)
    
# b = json.dumps(data)
# print(b)

data[0].append({
    
    "4":"space"
})

with open('congo.json', W) as file:
    json.dump(data,file)
    
    
    