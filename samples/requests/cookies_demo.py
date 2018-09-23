import requests

# r =requests.get('https://www.zhihu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key,'=',value)

#region 将cookie设置在headers中, 正常登录知乎
headers = {
    'Cookie': 'd_c0="AFDC4zX2KQuPTlbfROuoNlMOJ-VbpL1qaaI=|1484574567"; _zap=21acf10c-5edb-485f-8992-ee3dde28d70d; q_c1=1f85e3d7f07b434c941552234b2e0952|1505036360000|1484574567000; __utmv=51854390.100-1|2=registration_date=20141018=1^3=entry_date=20141018=1; _xsrf=ST3Bfbo7AUhCaRGCREtDsvptlWKNGGFo; l_cap_id="OTYxMTBlYTRiN2UyNDczYWI5ZDkyODMyYmJhYTMyNzA=|1535301188|1ee8560289a17516813415ddc9ebe45116148c74"; r_cap_id="M2QxNGM0ZDVhMGE5NDk0NTg0OGJhYTY2NDc5ZDdhODM=|1535301188|d774ee2d8b7da3fff8e2bc9bba556318c3eb6191"; cap_id="ZTU1NDIyNDEyYWFiNDZlNGI4YThjMDNkOTI1ODEzMGY=|1535301188|9661393d3e92023f9caac071fbef8f641a0a4c57"; capsion_ticket="2|1:0|10:1536509287|14:capsion_ticket|44:YzU0MGEyZmNiYTQ4NDFmMjkwMWZlYzA3N2QyYzZkZWM=|d785e564c74a9b7cbbccabc73243e899c85c565a93cfb519b226219072f1fa6c"; z_c0="2|1:0|10:1536509289|4:z_c0|92:Mi4xVHZDSkFBQUFBQUFBVU1Mak5mWXBDeVlBQUFCZ0FsVk5hWk9DWEFDN1hDLWV5OWVvalJuWDBUSmhoUnU5OTA4aENB|bc1f30b8dbd7cc56239279b69c3ea825283d9c0dbb7a66811fc29332c38d03c9"; q_c1=1f85e3d7f07b434c941552234b2e0952|1536509289000|1484574567000; __utma=51854390.2044456871.1487607357.1523685286.1536509642.21; __utmz=51854390.1536509642.21.8.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/wang-du-tu/collections; tgw_l7_route=8605c5a961285724a313ad9c1bbbc186',
    'Referrer': 'https://www.zhihu.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

response = requests.get('https://www.zhihu.com', headers=headers)
print(response.text)
#endregion

#region cookie设置在请求参数中，登录知乎并未生效
# headers = {
#     'Referrer': 'https://www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
# }
# cookies = 'd_c0="AFDC4zX2KQuPTlbfROuoNlMOJ-VbpL1qaaI=|1484574567"; _zap=21acf10c-5edb-485f-8992-ee3dde28d70d; q_c1=1f85e3d7f07b434c941552234b2e0952|1505036360000|1484574567000; __utmv=51854390.100-1|2=registration_date=20141018=1^3=entry_date=20141018=1; _xsrf=ST3Bfbo7AUhCaRGCREtDsvptlWKNGGFo; l_cap_id="OTYxMTBlYTRiN2UyNDczYWI5ZDkyODMyYmJhYTMyNzA=|1535301188|1ee8560289a17516813415ddc9ebe45116148c74"; r_cap_id="M2QxNGM0ZDVhMGE5NDk0NTg0OGJhYTY2NDc5ZDdhODM=|1535301188|d774ee2d8b7da3fff8e2bc9bba556318c3eb6191"; cap_id="ZTU1NDIyNDEyYWFiNDZlNGI4YThjMDNkOTI1ODEzMGY=|1535301188|9661393d3e92023f9caac071fbef8f641a0a4c57"; capsion_ticket="2|1:0|10:1536509287|14:capsion_ticket|44:YzU0MGEyZmNiYTQ4NDFmMjkwMWZlYzA3N2QyYzZkZWM=|d785e564c74a9b7cbbccabc73243e899c85c565a93cfb519b226219072f1fa6c"; z_c0="2|1:0|10:1536509289|4:z_c0|92:Mi4xVHZDSkFBQUFBQUFBVU1Mak5mWXBDeVlBQUFCZ0FsVk5hWk9DWEFDN1hDLWV5OWVvalJuWDBUSmhoUnU5OTA4aENB|bc1f30b8dbd7cc56239279b69c3ea825283d9c0dbb7a66811fc29332c38d03c9"; q_c1=1f85e3d7f07b434c941552234b2e0952|1536509289000|1484574567000; __utma=51854390.2044456871.1487607357.1523685286.1536509642.21; __utmz=51854390.1536509642.21.8.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/wang-du-tu/collections; tgw_l7_route=8605c5a961285724a313ad9c1bbbc186'
# jar = requests.cookies.RequestsCookieJar()
# for cookie in cookies.split():
#     key, value = cookie.split('=', maxsplit=1)
#     jar.set(key, value)
#     print(key,'=',value)
# r = requests.get('https://www.zhihu.com', cookies=jar, headers=headers, allow_redirects=False)
# print(r.text)
#endregion