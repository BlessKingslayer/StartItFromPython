import urllib.request
import urllib.parse

data = bytes(urllib.parse.urlencode({'name': 'chong'}, doseq=False, safe='', encoding='utf8', errors=None), encoding='utf8')

response = urllib.request.urlopen('http://httpbin.org/post', data=data, cafile=None, capath=None, cadefault=False, context=None)

print(response.read())