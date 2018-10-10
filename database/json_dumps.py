import json
import sys
sys.path.append('../utils')
import CreateFile

data = [{
    'name': '王家伟',
    'gender': 'male',
    'birthday': '1992-10-18'
}]
path = CreateFile.createFile('data2.json')
with open(path, 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))