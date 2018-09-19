import requests

data = {
    'name': 'jiawei',
    'age': 34
}

r = requests.post('http://httpbin.org/post', data=data)
print(r.text)
print(type(r.cookies))
print(requests.codes)