import requests
from lxml import etree
import re
import urllib.parse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Host': 'www.tmsf.com',
    'Referer': 'http://www.tmsf.com/newhouse/property_330184_20162341_price.htm',
    'Cookie': 'gr_user_id=52072b65-d88b-4b29-aa04-7e5f47b86a27; grwng_uid=28d4cded-bd69-4a94-8df2-ad84fa45786b; UM_distinctid=16657b7e9f5953-08b9cfeb10ca31-333b5402-100200-16657b7e9f7887; CNZZDATA1253675216=787924961-1539069193-http%253A%252F%252Fwww.tmsf.com%252F%7C1539069193; Hm_lvt_bbb8b9db5fbc7576fd868d7931c80ee1=1539069951,1539139916; Hm_lvt_e2f064987fcc6204fb690aa68ec76ac3=1539069954,1539139929; Hm_lpvt_e2f064987fcc6204fb690aa68ec76ac3=1539142523; JSESSIONID=FFC7177A72306805ED596871485DAEC5; Hm_lpvt_bbb8b9db5fbc7576fd868d7931c80ee1=1539151762'
}

class HouseInfo(object):
    __slots__ = ('building_no', 'house_no', 'floor_area', 'inside_floor_area', 'efficiency',
                'billet_price', 'decoration_price', 'total', 'operation')

    def __init__(self, info):
        self.building_no = info[0]
        self.house_no = info[1]
        self.floor_area = info[2]
        self.inside_floor_area = info[3]
        self.efficiency = info[4]
        self.billet_price = info[5]
        self.decoration_price = info[6]
        self.total = info[7]
        self.operation = info[8]

# 获取幢号({id: 楼号})
def get_house_nums():
    mainUrl = get_url()
    response = requests.get(mainUrl, headers=headers)
    html = etree.HTML(response.content)
    houseNumNode = html.xpath('//div[@id="building_dd"]//a[position()>1]')
    houseDict = {}
    for item in houseNumNode:
        houseDict[item.xpath('@id')[0]] = item.xpath('text()')[0]
    return houseDict

# 拆分url参数(为什么不用parse_qs？)
# 因为 parmsDict = urllib.parse.parse_qs(result.group('params')) # 只能返回值不为空的参数
def split_urlparams(url):
    regstr = re.compile('(?P<main>.*?\?)(?P<params>.*)')
    result = re.match(regstr, url)

    mainStr = result.group("main")
    paramStr = result.group('params')

    paramList = paramStr.split('&')
    paramKeys = [item.split('=')[0] for item in paramList]
    paramVals = [item.split('=')[1] for item in paramList]
    parmsDict = {}
    for i in range(len(paramList)):
        parmsDict[paramKeys[i]] = paramVals[i]
    return parmsDict

# 替换url参数
def get_url(paramDict=None, originDict=None):
    mainUrl = 'http://www.tmsf.com/newhouse/property_330184_20162341_price.htm?isopen=&presellid=12502662&buildingid=&area=&allprice=&housestate=&housetype=&page='
    if mainUrl is not None:
        return mainUrl

    if len(paramDict) > 0:
        for k, v in paramDict:
            originDict[k] = v
    return '{0}?{1}'.format(mainStr, urllib.parse.urlencode(originDict))

# 获取

def main():

    houseDict = get_house_nums()
    originDict = split_urlparams(get_url())
    targetUrls = []
    for item in houseDict.keys():
        print(item.split('_')[0], ',', item.split('_')[1])
        dic = {item.split('_')[0]: item.split('_')[1]}
        targetUrls.append(get_url(dic, originDict))

    print(targetUrls)


main()