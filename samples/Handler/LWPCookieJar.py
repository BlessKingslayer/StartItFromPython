import http.cookiejar
import urllib
import sys, imp, io


# 获得系统编码格式
type = sys.getfilesystemencoding()
sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer, encoding='utf-8')  #改变标准输出的默认编码

cookie2 = http.cookiejar.LWPCookieJar()
cookie2.load('cookies2.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie2)
opener = urllib.request.build_opener(handler)
response = opener.open('https://baidu.com')
print(response.read().decode('utf-8', 'ignore'))