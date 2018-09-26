import requests
from requests.packages import urllib3

urllib3.disable_warnings() # 忽略不检查证书导致的警告
try:
    r = requests.get('https://www.12306.cn', verify=False)  # 不检查ssl证书
    #region 示例代码 指定本地证书
    # response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key')) 
    #endregion
    print(r.status_code)
except requests.exceptions.SSLError as ex:
    print(ex)