import requests
import json
import time

f = open('csfcookie.csv','r')
fp = f.read()
fp = fp.split("\n")
for i in range(0,len(fp)):
    print(fp[i])
print(fp)
time.sleep(0.1)
url = "http://test.wemew.cn/cwechat/pascreenPay"
url1 = "http://test.wemew.cn/cwechat/getNewYearUserGift"
payload = {
    'sitnum': '',
    'second': 10,
    'msg': '涓�澶滆緱杞簲鍏満锛屾壎澧欒刀寰�涓嬩竴鍦�',
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
headers = {
    'accept': "*/*",
    'x-requested-with': "XMLHttpRequest",
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'Cookie': 'T_USERID=%s'% fp +'; T_BARBASEID_NEW=1165F4CDB486AAE7FA91BD302C131FBF43FFC1DEFD0E6D79A2DE498C324EFD3CDDEF1863B90F9D86; admin_barbaseid=1165F4CDB486AAE7FA91BD302C131FBF43FFC1DEFD0E6D79A2DE498C324EFD3CDDEF1863B90F9D86; SCREENV=9ABF513678239B98320056C84D7CF8E39529B4F170ED4670CC2F07CA044F02E8E41A2E6A9773AF56; AU=4A52B01760B5DCC7C887DE76FC707951EDD8A8C74DBCE02784DE03C6F7867980852AE7594871BFCC1FBA94F2A4BC23BD; b_l_sid=2C7233C42BF0550960CF74C64F175959332CFD4A527FC4E5FBB093899B0666925F1A3FABD07589C2; Hm_lvt_bbcfda495d9cf0463dc64c3b6b0c4187=1576647978,1576648392,1576669911,1576718905; JSESSIONID=5D5926F46A08F977E052C96919B5BB39; Hm_lpvt_bbcfda495d9cf0463dc64c3b6b0c4187=1576737554'    
    }
headers = {
    'accept': "*/*",
    'x-requested-with': "XMLHttpRequest",
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'Cookie': 'T_USERID=%s'% fp +'; T_BARBASEID_NEW=93285C0FAFFA8297AB5BDD28A925C3F61DBD3C549A8CB5AA0DDE579C5EC2726F750726AA6751792F;07CA044F02E8E41A2E6A9773AF56;' ,
     }
test1 = 0
test2 = 0
test3 = 0
test4 = 0
test5 = 0
test6 = 0
test7 = 0
i=0
test8=0

while i<100:
#     headers = {
#     'accept': "*/*",
#     'x-requested-with': "XMLHttpRequest",
#     'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
#     'content-type': "application/x-www-form-urlencoded",
#     'cache-control': "no-cache",
#     'Cookie': 'T_USERID=%s'% fp[i] +'; T_BARBASEID_NEW=1165F4CDB486AAE7FA91BD302C131FBF43FFC1DEFD0E6D79A2DE498C324EFD3CDDEF1863B90F9D86; admin_barbaseid=1165F4CDB486AAE7FA91BD302C131FBF43FFC1DEFD0E6D79A2DE498C324EFD3CDDEF1863B90F9D86; SCREENV=9ABF513678239B98320056C84D7CF8E39529B4F170ED4670CC2F07CA044F02E8E41A2E6A9773AF56; AU=4A52B01760B5DCC7C887DE76FC707951EDD8A8C74DBCE02784DE03C6F7867980852AE7594871BFCC1FBA94F2A4BC23BD; b_l_sid=2C7233C42BF0550960CF74C64F175959332CFD4A527FC4E5FBB093899B0666925F1A3FABD07589C2; Hm_lvt_bbcfda495d9cf0463dc64c3b6b0c4187=1576647978,1576648392,1576669911,1576718905; JSESSIONID=5D5926F46A08F977E052C96919B5BB39; Hm_lpvt_bbcfda495d9cf0463dc64c3b6b0c4187=1576737554'    
#     }
    headers = {
    'accept': "*/*",
    'x-requested-with': "XMLHttpRequest",
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'Cookie': 'T_USERID=%s'% fp[i] +'; T_BARBASEID_NEW=93285C0FAFFA8297AB5BDD28A925C3F61DBD3C549A8CB5AA0DDE579C5EC2726F750726AA6751792F;07CA044F02E8E41A2E6A9773AF56;' ,
     }
    response = requests.request("POST", url, data=payload, headers=headers)
    response1 = requests.request("POST", url1, headers=headers).json()
    res = response1['resultMsg']
    res = json.loads(res)
    res = res['giftName']
    
    if res == '8.8鍏冨柕甯佺孩鍖�':
        test1 +=1
    elif res == '3.5鍏冨柕甯佺孩鍖�':
        test2 +=1   
    elif res == '2.5鍏冨柕甯佺孩鍖�':
        test3 +=1
    elif res == '1.2鍏冨柕甯佺孩鍖�':
        test4 +=1
    elif res == '0.5鍏冨柕甯佺孩鍖�':
        test5 +=1
    elif res == '8s闇稿睆寤舵椂鍒�':
        test6 +=1
    elif res == '鐨囧骞诲奖':
        test7 +=1
    elif res == '鍏堥┍闊抽��':
        test8 += 1
    else:
        print(res)
#     print(response.text)
#     print(response1)
#     print(res)
#     print(i,'----',test1,test2,test3,test4,test5,test6,test7)
    i+=1
    time.sleep(3)
    print(i,'----','8.8:',test1,'  3.5:',test2,'  2.5:',test3,'  1.2:',test4,'  0.5:',test5,'  8s:',test6,'  骞诲奖:',test7,'鍏堥┍' ,test8)

