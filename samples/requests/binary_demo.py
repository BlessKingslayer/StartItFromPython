import requests

r = requests.get('https://github.com/favicon.ico')
print(r.content)

with open('github_favicon.ico', 'wb') as f:
    f.write(r.content)