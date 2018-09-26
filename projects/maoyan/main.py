import requests
import re
import json
import time
from requests.exceptions import RequestException

def get_one_url(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as ex:
        print(ex)
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?'+ \
        '<a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>' + \
        '.*?fraction.*?>(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    # print(items)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'name': item[2].strip(),
            'star': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'releasetime': item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score': str.format('{0}{1}', item[5].strip(), item[6].strip())
        }

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        # print(json.loads(json.dumps(content)))
        print(json.dumps(content, ensure_ascii=False))
        # ensure_ascii=False 保证输出中文不是unicode格式
        f.write(json.dumps(content, ensure_ascii=False) + '\n') 

def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_url(url)
    # print(html)
    for content in parse_one_page(html):
        write_to_file(content)

if __name__ == '__main__':
    for i in range(10): # 0~9        
        main(offset = i * 10)
        time.sleep(1)