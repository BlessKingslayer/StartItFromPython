from urllib.request import HTTPBasicAuthHandler,HTTPPasswordMgrWithDefaultRealm, build_opener
from urllib.error import URLError

# 网站验证

username = 'username'
password = 'password'
url = 'http://localhost:5000/'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as ex:
    print(ex.reason)
