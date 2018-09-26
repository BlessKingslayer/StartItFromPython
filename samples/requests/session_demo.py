import requests

#region 无会话模式
# r = requests.get('http://httpbin.org/cookies/set/numbers/tt009')  # 发送给服务器数据设置cookie
# r = requests.get('http://httpbin.org/cookies')

# print(r.text)  # 获取到cookie为空
#endregion

#region 会话模式
s = requests.Session()
s.get('http://httpbin.org/cookies/set/numbers/tt009')
r = s.get('http://httpbin.org/cookies')
print(r.text) # 成功设置cookie
#endregion