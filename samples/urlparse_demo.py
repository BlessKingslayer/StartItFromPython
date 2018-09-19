import urllib.parse

result = urllib.parse.urlparse(
    'http://www.baidu.com/index.html;user?id=5#comment')

print(type(result), result)

res = urllib.parse.urlparse('https://xx.com?is=9&qwe=0')
print(res)
