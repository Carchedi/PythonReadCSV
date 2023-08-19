f = open("base.csv", "r")
result = open("translation.json", "w")

content = f.read()
items = content.split("\n") 
items.pop()

result.write('{\n')
for i in items:
    j = i.split(',')
    result.write('\t\"'+j[0]+'\": \"'+j[1]+'\",\n')
result.write('}')