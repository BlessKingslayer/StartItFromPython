import requests

Headers = {
    'User-Agent':
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.2)',
    'Referer':
    'https://fpdk.jsgs.gov.cn:81/fphx.b615b0ca.html',
    'Host':
    'fpdk.jsgs.gov.cn:81',
    'Cookie':
    'dzdzsl=20111189; dqrq=2018-10-29; nsrmc=%u6C5F%u82CF%u5357%u901A%u516D%u5EFA%u5EFA%u8BBE%u96C6%u56E2%u6709%u9650%u516C%u53F8; skssq=201810%3B20181115%3B201810; gxrqfw=20171006-20181031; token=1%7E0%7E0%7E%7E1%7E0%7E0%7E0%7E0%7E0%7Eaea27f34-b4fc-4c32-a1f7-afb0c08eab3e; yfx_c_g_u_id_10003709=_ck18011615030710075726531379081; yfx_f_l_v_t_10003709=f_t_1516086186891__r_t_1534236410623__v_t_1534236410623__r_c_34',
    'Remote Address':
    'fpdk.jsgs.gov.cn/221.226.83.22:81'
}
url = 'https://fpdk.jsgs.gov.cn:81/SbsqWW/gxcx.do?callback=jQuery110207837615178941363_1540800070933'
data = {
    'fpdm':
    '',
    'fphm':
    '',
    'rq_q':
    '2018-10-01',
    'rq_z':
    '2018-10-29',
    'xfsbh':
    '',
    'rzfs':
    '0',
    'rzzt':
    '1',
    'gxzt':
    '',
    'fpzt':
    '0',
    'fplx':
    '-1',
    'cert':
    '91320682711592946A',
    'token':
    '1~0~0~~1~0~0~0~0~0~aea27f34-b4fc-4c32-a1f7-afb0c08eab3e',
    'auData': '[{"name":"sEcho","value":1},{"name":"iColumns","value":14},{"name":"sColumns","value":",,,,,,,,,,,,,"},{"name":"iDisplayStart","value":0},{"name":"iDisplayLength","value":50},{"name":"mDataProp_0","value":0},{"name":"mDataProp_1","value":1},{"name":"mDataProp_2","value":2},{"name":"mDataProp_3","value":3},{"name":"mDataProp_4","value":4},{"name":"mDataProp_5","value":5},{"name":"mDataProp_6","value":6},{"name":"mDataProp_7","value":7},{"name":"mDataProp_8","value":8},{"name":"mDataProp_9","value":9},{"name":"mDataProp_10","value":10},{"name":"mDataProp_11","value":11},{"name":"mDataProp_12","value":12},{"name":"mDataProp_13","value":13}]',
    'ymbb':
    '3.1.10',
    'ts':
    '1540799316530',
    'publickey':
    # 'ba0698460c6fd3e901e0198a1952573d'
    'ba0698460c6fd3e901e0198a1952573d'
}
response = requests.get(
    url,
    headers=Headers,
    params=data,
    # data=data,
    verify=False
    # 'G:\\EveryDayCode\\JustPython\\StartItFromPython\\projects\\fpdk\\target.pem'
)

print(response.text)