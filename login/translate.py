# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 15:00:55 2022

@author: 20277
"""

import requests
import hashlib
import random
import time

def translate1(i, from_ = 'zh-CHS', to = 'ko'):
    #i = '你叫什么'
    s = requests.Session()
    m = hashlib.md5()
    ts = str(int(time.time()*1000))
    salt = ts + str(random.randint(1,10))
    n = 'fanyideskweb' + i + salt + "Y2FYu%TNSbMCxc3t2u^XT"
    m.update(n.encode('utf-8'))
    sign = m.hexdigest()
    
    headers = {
        'Host': 'fanyi.youdao.com',
        'Cookie':'OUTFOX_SEARCH_USER_ID=401449051@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=1779031387.2494004; JSESSIONID=aaa0ubyHUu7Td4GyOxG4x; ___rl__test__cookies=1641222755942',
        'Origin': 'https://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    data = {'i':i,
            'from':from_,
            'to':to,
            'smartresult':'dict',
            'client':'fanyideskweb',
            'salt':salt,
            'sign':sign,
            'lts':ts,
            'bv':'53539dde41bde18f4a71bb075fcf2e66',
            'doctype':'json',
            'version':'2.1',
            'keyfrom':'fanyi.web',
            'action':'FY_BY_REALTlME'}
    r = requests.post(url, headers=headers,data=data)
    if r.status_code == 200:
        if r.json()['errorCode'] == 0:
            return r.json()['translateResult'][0][0]['tgt']
        else:
            print('error')
            return False
    else:
        print('未响应')
        return False
def translate_bd(i):
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    appid = '20201230000659637'
    key = 'jc2uIslzscbLoQtTNY4z'
    salt = str(random.randint(1,10))
    s = appid + i + salt + key
    m = hashlib.md5()
    m.update(s.encode('utf-8'))
    sign = m.hexdigest()
    data = {
        'from':'kor',
        'to':'de',
        'q':i,
        'appid':appid,
        'salt':salt,
        'sign':sign
        }
    r = requests.post(url, data)
    if r.status_code == 200:
        return r.json()['trans_result'][0]['dst']
    else:
        print('BaiduError')
        return False
    
def translate2(i):
    t1 = translate1(i)   #中文转韩文
    print(t1)
    if t1 != False:        
        t2 = translate_bd(t1)   #韩文转德文
        print(t2)
    if t2 != False:
        t3 = translate1(from_ = 'de', to = 'zh-CHS',i = t2) #德文转中文
        print(t3)
    if t3 != False:
        return t3
    else:
        return False
        
    
def main(i):
    n = 6
    while True:
        result = translate2(i)
        n -= 1
        time.sleep(2)
        if result != False:
            return result
        if n < 0:
            return 'ERROR!'
    