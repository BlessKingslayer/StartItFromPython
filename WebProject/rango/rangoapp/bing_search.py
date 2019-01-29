import json
import requests
from urllib import parse

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
        print(e.value)
        return []

# run_query('湖人')
