import requests
from pyquery import PyQuery as pq
import sys
sys.path.append("../utils")
import CreateFile

url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
html = requests.get(url, headers = headers).text
doc = pq(html)
items = doc('.explore-tab .feed-item').items()

for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    path = CreateFile.createFile(filename = 'explore.txt')
    with open(path, 'a', encoding='utf-8') as file:
        file.write('\n'.join([question, author, answer]))
        file.write('\n' + '=' * 50 + '\n')
