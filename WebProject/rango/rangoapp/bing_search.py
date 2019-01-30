import json
import requests
import urllib, re
from urllib import parse
from bs4 import BeautifulSoup as BS

subscriptionKey = '3284bc328b4e42cdbb7f4b146244f1a7'
customConfigId = '11f16227-8322-496c-a278-22259435252d'
# searchTerm = "湖人"

# url = 'https://api.cognitive.microsoft.com/bingcustomsearch/v7.0/search?' \
#     + 'q=' + searchTerm + '&' + 'customconfig=' + customConfigId + '&' + 'count=10'

# r = requests.get(url, headers={'Ocp-Apim-Subscription-Key': subscriptionKey})
# print(r.text)

# a = json.loads(r.text)


def run_query(search_terms, count=10):
    try:
        urlbase = 'https://api.cognitive.microsoft.com/bingcustomsearch/v7.0/search?'
        parms = {'customconfig': customConfigId, 'count': count, 'q': search_terms}
        url = urlbase + parse.urlencode(parms)
        r = requests.get(
            url, headers={'Ocp-Apim-Subscription-Key': subscriptionKey})
        resobj = json.loads(r.text)
        return resobj['webPages']['value']
    except Exception as e:
        print(e)
        return []


def run_query2(search_terms):
    url = 'https://cn.bing.com/search?'
    parms = {
        'q': search_terms,
        'go': '搜索',
        'qs': 'ds',
        'form': 'QBRE'
    }
    url = url + parse.urlencode(parms)
    # r = requests.get(url)
    try:
        html = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print(e.code)
    except urllib.error.URLError as e:
        print(e.reason)

    soup = BS(html, "html.parser")
    td = soup.findAll("h2")
    count = soup.findAll(class_="sb_count")
    for c in count:
        print(c.get_text())

    for t in td:
        print(t.get_text())
        pattern = re.compile(r'href="([^"]*)"')
        h = re.search(pattern,str(t))
        if h:
            for x in h.groups():
                print(x)

run_query2('湖人')
