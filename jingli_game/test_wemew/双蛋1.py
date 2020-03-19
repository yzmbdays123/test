import requests
import json
import time
import csv
url = "http://test.wemew.cn/cwechat/pascreenPay"
url1 = "http://test.wemew.cn/cwechat/whiteDayLastUserGift"
url2 = 'https://test.wemew.cn/cwechat/whiteDayGrabBagRain'

payload = {
    'sitnum': '',
    'second': 10,
    'msg': '一夜辗转五六场，扶墙赶往下一场',
    'img': '',
    'msgid':'' ,
    'showNum': 1,
    'videoUrl': '',
    'xttype': 1,
    'seatNumber':'' ,
    'cigarettePrice': -1,
    'usePascreenExperience': 'false',
    'isDoubleOne': 0,
    'isCheckVip': 'false',
    'btnNum':'' ,
    'isMiniApp': 'false',
    
    }
with open(r'测试服cookie.csv','r') as a:
#     d = csv.reader(a)
    b = a.readlines()
    for j in b:
#         c=j.replace('\n','')

        print(j)
        
        test1 = 0
        test2 = 0
        test3 = 0
        test4 = 0
        test5 = 0
        test6 = 0
        test7 = 0
        i=0
        headers = {
    'accept': "*/*",
    'x-requested-with': "XMLHttpRequest",
    'user-agent': "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36",
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'Cookie': 'T_USERID=848EE53AF81A92DD2A221F8EA3C5403C6CD1A4D3EBC3E8D134A89AEE874DE244B632193C4BF63494;T_BARBASEID_NEW=1165F4CDB486AAE7FA91BD302C131FBF43FFC1DEFD0E6D79A2DE498C324EFD3CDDEF1863B90F9D86;'  
        }

        

        print('jjj',j)
        response3 = requests.request("POST", url2, headers=headers).json()
        print(response3)
        response = requests.request("POST", url, data=payload, headers=headers)
        response1 = requests.request("POST", url1, headers=headers).json()

        res = response1['resultMsg']
        res = json.loads(res)
        res = res['giftName']
        
#         if res == '8.8元喵币红包':
#             test1 +=1
#         elif res == '3.5元喵币红包':
#             test2 +=1   
#         elif res == '2.5元喵币红包':
#             test3 +=1
#         elif res == '1.2元喵币红包':
#             test4 +=1
#         elif res == '0.5元喵币红包':
#             test5 +=1
#         elif res == '8s霸屏延时券':
#             test6 +=1
#         elif res == '邪恶之眼':
#             test7 +=1
#         else:
#             print('出错了')
#         print(j)
        print(response1)
        print(res)
        print(i,'----',test1,test2,test3,test4,test5,test6,test7)
        time.sleep(3)
    print('8.8:',test1,'  3.5:',test2,'  2.5:',test3,'  1.2:',test4,'  0.5:',test5,'  8s:',test6,'  邪恶:',test7)

