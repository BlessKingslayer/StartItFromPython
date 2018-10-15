import requests
from lxml import etree
import chardet
import sys
import io
import re
from fontTools.ttLib import TTFont
sys.path.append("G:\\EveryDayCode\\JustPython\\StartItFromPython\\utils")
import CreateFile
import fontface
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')


Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Authority': 'hz.58.com',
    'Path': '/qzitjishuweihu/?PGTID=0d303349-0004-ffe2-1a2c-3cf60cddc6aa&ClickID=2',
    'Cookie': 'f=n; commontopbar_new_city_info=79%7C%E6%9D%AD%E5%B7%9E%7Chz; commontopbar_ipcity=hz%7C%E6%9D%AD%E5%B7%9E%7C0; id58=c5/nn1q9rMMHrw73HJ1sAg==; sessionid=c15c852e-19ec-4782-b76c-b519d3ca5eeb; param8616=1; param8716kop=1; 58tj_uuid=f0858893-5046-4aa5-a4ae-67ad7c738198; new_uv=1; utm_source=; spm=; init_refer=; als=0; wmda_uuid=302a4f628bb6dab38719f7d2932a7e57; wmda_new_uuid=1; wmda_session_id_1731916484865=1539571148358-aedaac55-d282-f346; wmda_visited_projects=%3B1731916484865; f=n; isSmartSortTipShowed=true; new_session=0; xxzl_deviceid=TxAH5kPMpIkrRzi7xbJidgmkdt%2BLxLL9Kx1yK2tFjpF8nij6GlCJ6V5puwl3r8Nm; 58cooper="userid=58911192361743&username=nrmclfi2d&cooperkey=d31acdaaba1eb16c748c7eeb081d84a3"; Hm_lvt_a3013634de7e7a5d307653e15a0584cf=1539571148,1539571776; JSESSIONID=4B8CC110DB572488BAD15EEEF20B9A35; jl_list_left_banner=7; Hm_lpvt_a3013634de7e7a5d307653e15a0584cf=1539572209; xxzl_smartid=8b4aa36aa71d5e65c67dd6f951a8c0e8; ppStore_fingerprint=E9E8AACCAE891A2B3072877331F73822DAA26A6ED9089137%EF%BC%BF1539572250603; PPU="UID=58911192361743&UN=nrmclfi2d&TT=42c03ae3998da1377ee8afffe5ae3d23&PBODY=MfeY_JXcjH2s0yCosNq9CdF4bnDoNY0Xuxgm8EboPp9pgLNnnKaOv5kYqWZI5eR6i5U2OzTNE-w6v5QU3p3XnYzy4nWms5gQeasNOlMc1yzzoOHWfNbrBuCFf1-0f7EjGIU1IX0l6mmZTswv9-j2B3c2WsCYqq12uJcZXSmMr9k&VER=1"; www58com="AutoLogin=true&UserID=58911192361743&UserName=nrmclfi2d&CityID=0&Email=&AllMsgTotal=0&CommentReadTotal=0&CommentUnReadTotal=0&MsgReadTotal=0&MsgUnReadTotal=0&RequireFriendReadTotal=0&RequireFriendUnReadTotal=0&SystemReadTotal=0&SystemUnReadTotal=0&UserCredit=0&UserScore=0&PurviewID=&IsAgency=false&Agencys=null&SiteKey=3FFB2E44A074375AA1D7440012AB38A6940D72ACD87D16741&Phone=&WltUrl=&UserLoginVer=1FC200CCC2CA2C7E985EFDA6D29953708&LT=1539572247160"; ljrzfc=1; showPTTip=1'
}
MainUrl = 'https://hz.58.com/qzitjishuweihu/?PGTID=0d303349-0004-ffe2-1a2c-3cf60cddc6aa&ClickID=2'

def get_xpath_obj(url):
    global Headers
    response = requests.get(url, headers=Headers)
    print(chardet.detect(response.content))
    html = etree.HTML(response.content)
    return html

# 生成字体文件xml
def create_ttf_xml(html):
    fontstr = html.xpath('//style[1]/text()')[0]
    pattern = re.compile('^.*?base64,(.*?)\).*?format', re.S)
    result = re.match(pattern, fontstr)
    str = result.group(1)
    dic = fontface.createTtfAndXml(str)

    if dic['ttf'] == '':
        raise RuntimeError('字体文件不存在！')
    fonts = TTFont(dic['ttf'])
    uni_list = fonts.getGlyphOrder()[1:]
    for uni in uni_list:
        obj2 = fonts['glyf'][uni]
        print(obj2)


def get_main_list(url):
    html = get_xpath_obj(url)
    nodes = html.xpath('//div[@id="infolist"]/dl/dd/text()')
    print(nodes)
    create_ttf_xml(html)


def main():
    global MainUrl
    get_main_list(MainUrl)

if __name__ == '__main__':
    main()