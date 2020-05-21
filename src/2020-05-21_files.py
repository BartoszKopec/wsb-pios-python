import json

def getFile(file):
    try:
        with open(file, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return ''

def setFile(file, text):
    with open(file, 'w') as f:
        f.write(text)

filePath = 'data.json'

dataStr = getFile(filePath)
if dataStr == '':
    dict = {
        'name': 'messenger',
        'playstore': True,
        'company': 'Facebook',
        'price': 100
    }
    dataStr = json.dumps(dict)
    setFile(filePath, dataStr)
data = json.loads(dataStr)
print('Data saved in json file:')
for key,value in data.items():
    print(key, ':', value)


