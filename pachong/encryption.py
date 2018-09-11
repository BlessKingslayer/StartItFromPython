# -*- coding: utf-8 -*-

import execjs
import requests

# Init 环境
node = execjs.get()

method = 'GETCITYWEATHER'
city = '杭州'
type = 'HOUR'
start_time = '2018-09-11 00:00:00'
end_time = '2018-09-11 23:00:00'

file = 'encryption.js'
ctx = node.compile(open(file, encoding='UTF-8').read())

js = 'getEncryptedData("{0}", "{1}", "{2}", "{3}", "{4}")'.format(method, city, type, start_time, end_time)
params = ctx.eval(js)

# Get encrypted response text
api = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
response = requests.post(api, data={'d': params})

# Decode data
js = 'decodeData("{0}")'.format(response.text)
decrypted_data = ctx.eval(js)

print(decrypted_data.encode('utf-8').decode('unicode_escape'))
