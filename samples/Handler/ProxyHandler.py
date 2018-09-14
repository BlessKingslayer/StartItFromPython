from urllib.request import ProxyHandler, build_opener
from urllib.error import URLError

proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'https://127.0.0.1:9743'
})

opener = build_opener(ProxyHandler)
try:
    response = opener.open('https://baidu.com')
    print(response.read().decode('gbk', 'ignore'))  # .encode('GBK', 'ignore')
except URLError as ex:
    print(ex.reason)