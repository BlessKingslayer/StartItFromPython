import requests

r = requests.get('https://baidu.com')
print(type(r))
print(r.status_code)
print(type(r.text))
# print(r.text)
print(r.cookies)

data = {
    'name': 'liming',
    'age': 23
}

r = requests.get('http://httpbin.org/get', params=data)
print(r.text)
print(r.json())
print(type(r.json()))