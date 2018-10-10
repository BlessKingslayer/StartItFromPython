import json
import sys
sys.path.append('../utils')
import CreateFile

str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
print(type(str))
data = json.loads(str)
print(type(data))
print(data[0]["name"])
print(data[0].get("name"))
print(type(data[0]))
print('-' * 100)

with open(CreateFile.createFile("data.json"), 'r') as file:
    str = file.read()
    data = json.loads(str) if str.strip() != '' else '文件内容为空'
    print(type(data))
    print(data[0]['name'])