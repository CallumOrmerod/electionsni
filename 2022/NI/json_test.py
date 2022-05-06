import json

f = open('../../2017/NI/all-candidates.json')
g = open('all-candidates.json')

print (f)
print(g)

data = json.load(f)
print(data)

data22 = json.load(g)
#print(data22)