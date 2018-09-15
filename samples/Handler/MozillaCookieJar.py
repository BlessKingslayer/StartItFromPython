import http.cookiejar
import urllib

# filename = 'cookies.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)

filename = 'cookies2.txt'
cookie = http.cookiejar.LWPCookieJar(filename)

handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)