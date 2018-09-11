from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import requests
from lxml import etree

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome(chrome_options=chrome_options)

cururl = 'https://github.com/login'
session = requests.Session()
try:
    browser.get(cururl)
    utf8_data = browser.find_element_by_name('utf8').get_attribute('value')
    token_data = browser.find_element_by_name('authenticity_token').get_attribute('value')
    commit_data = browser.find_element_by_name('commit').get_attribute('value')
    login_data = '836432552@qq.com'#browser.find_element_by_name('login').get_attribute('value')
    pwd_data = 'waaywjwnba914'#browser.find_element_by_name('password').get_attribute('value')
    #print('name: ', login_data)
    #print('pwd: ', pwd_data)
    print('token_data: ', token_data)
except WebDriverException as ex:
    print('异常: ', ex.msg)

headers = {
    'Refer': 'https://github.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Host': 'github.com'
}
post_url = 'https://github.com/session'
logined_url = 'https://github.com/settings/profile'
form_data = {
    "authenticity_token": token_data,
    "utf8": utf8_data,
    "commit": commit_data,
    "login": login_data,
    "password": pwd_data
}


def dynamics(html):  # 使用此方法提取所有动态信息
    selector = etree.HTML(html)
    dynamics = selector.xpath(
        '//div[contains(@class, "news")]//div[contains(@class, "alert")]')
    for item in dynamics:
        dynamics = ' '.join(
            item.xpath('.//div[@class="title"]//text()')).strip()
        print(dynamics)


def profile(html):  # 使用此方法提取个人的昵称和绑定的邮箱
    selector = etree.HTML(html)
    name = selector.xpath('//input[@id="user_profile_name"]/@value')[0]
    email = selector.xpath(
        '//select[@id="user_profile_email"]/option[@value!=""]/text()')
    print(name, email)


response = session.post(post_url, data=form_data, headers=headers)
print('dynamics: ', response.status_code)
if response.status_code == 200:
    print('dynamics: ', response.url)
    dynamics(response.text)

response = session.get(logined_url, headers=headers)
print('profile: ', response.status_code)
if response.status_code == 200:
    print('profile: ', response.url)
    profile(response.text)
