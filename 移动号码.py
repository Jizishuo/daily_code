import requests,json,time

def login():
    '''
    该函数能循环取出所有移动号码
    '''
    header = {'Host': 'service.micard.10046.mi.com', 'Connection': 'keep-alive', 'Content-Length': '62', 'Accept': 'application/x-www-form-urlencoded, application/json;q=0.8, text/plain;q=0.5, */*;q=0.2', 'Origin': 'http://service.micard.10046.mi.com', 'X-Requested-With': 'rest.js', 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded', 'Referer': 'http://service.micard.10046.mi.com/ctmiphone/cardSelling_form?channel_code=1003', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}


    url =  'http://service.micard.10046.mi.com/ctmiphone/get_numbers'
    data = 'province_code=23&city_code=271&page_index=1&limit=100000&condition='
    res = requests.post(url=url, headers=header,data=data)
    return res


s = login()
print(s.text)
s = json.loads(s.text)
'''
print(s['data']['phone_number_list'])
print(len(s['data']['phone_number_list']))
for i in range(2131):
    print(s['data']['phone_number_list'][i]['phone_number'])
    print(s['obj']['cardList']['list'])
    for i in s['obj']['cardList']['list']:
        print(i)
        with open('./移动号码.txt', 'a') as f:
            f.write(i + '\n')
    time.sleep(1)
'''
