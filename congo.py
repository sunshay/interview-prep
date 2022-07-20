import json
with open('congo.json') as file:
    data = json.load(file)
    
b = json.dumps(data)
print(b)