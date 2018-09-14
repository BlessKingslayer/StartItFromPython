import urllib.parse
import urllib.request
import urllib.error

datas = bytes(urllib.parse.urlencode({"name": "hello"}), encoding='utf8')

try:
    response = urllib.request.urlopen("http://httpbin.org/post", data=datas)
    print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(e.code, ", ", e.reason)
