import requests

files = {'file': open('github_favicon.ico', 'rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)