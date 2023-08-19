f = open("base.csv", "r")
result = open("translation.json", "w")

content = f.read()
items = content.split("\n") 
items.pop()

text = ('{\n')
for i in items:
    j = i.split(',')
    text += ('\t\"'+j[0]+'\": \"'+j[1]+'\",\n')
text = text[:-2]
text += '\n}'
result.write(text)