import pymysql
import requests
import time 
import json
#连接数据库

db = pymysql.connect("118.190.78.216","root","wemew4152639*","weixin")
#使用cursor()方法创建一个游标对象
cursor = db.cursor()
try:
    cursor.execute("DELETE from base_game_result ")
except:
    print('连接失败')
shouji_head ={
    'accept': "*/*",
    'x-requested-with': "XMLHttpRequest",
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'Cookie': 'T_USERID=E85775D6A7160C99048BDD8D6CFD48935D16E9DFDAF5365C834BA38CF0D7673D54AD76ECECF6D7D2; T_BARBASEID_NEW=1165F4CDB486AAE7FA91BD302C131FBF43FFC1DEFD0E6D79A2DE498C324EFD3CDDEF1863B90F9D86; admin_barbaseid=1165F4CDB486AAE7FA91BD302C131FBF43FFC1DEFD0E6D79A2DE498C324EFD3CDDEF1863B90F9D86; SCREENV=9ABF513678239B98320056C84D7CF8E39529B4F170ED4670CC2F07CA044F02E8E41A2E6A9773AF56; AU=4A52B01760B5DCC7C887DE76FC707951EDD8A8C74DBCE02784DE03C6F7867980852AE7594871BFCC1FBA94F2A4BC23BD; b_l_sid=2C7233C42BF0550960CF74C64F175959332CFD4A527FC4E5FBB093899B0666925F1A3FABD07589C2; Hm_lvt_bbcfda495d9cf0463dc64c3b6b0c4187=1576647978,1576648392,1576669911,1576718905; JSESSIONID=5D5926F46A08F977E052C96919B5BB39; Hm_lpvt_bbcfda495d9cf0463dc64c3b6b0c4187=1576737554'    
    }

diannao_head={
    'Cookie': 'Hm_lvt_bbcfda495d9cf0463dc64c3b6b0c4187=1578965845; T_USERID=E85775D6A7160C99048BDD8D6CFD48935D16E9DFDAF5365C834BA38CF0D7673D54AD76ECECF6D7D2; admin_barbaseid=1165F4CDB486AAE7FA91BD302C131FBF43FFC1DEFD0E6D79A2DE498C324EFD3CDDEF1863B90F9D86; AU=4A52B01760B5DCC7C887DE76FC707951EDD8A8C74DBCE02784DE03C6F7867980852AE7594871BFCC1FBA94F2A4BC23BD; b_l_sid=2C7233C42BF0550960CF74C64F175959332CFD4A527FC4E5FBB093899B0666925F1A3FABD07589C2; SCREENV=9ABF513678239B98320056C84D7CF8E39529B4F170ED4670CC2F07CA044F02E8E41A2E6A9773AF56; Hm_lpvt_bbcfda495d9cf0463dc64c3b6b0c4187=1578985766; T_BARBASEID_NEW=1165F4CDB486AAE7FA91BD302C131FBF43FFC1DEFD0E6D79A2DE498C324EFD3CDDEF1863B90F9D86; game=shakeGame; JSESSIONID=4EF467FF81F1C7247975B5F0F8B6D0A4',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
    }


start_data={
    'gameOnOff': 1,
    'timesId': 0,
    'barid': '53c2336a-5a67-4ca8-8677-1180c99bc583',
    'type': 1
    }
timeId = ''

jiesu_data={
    'gameOnOff': 1,
    'timesId': timeId,
    'barid': '53c2336a-5a67-4ca8-8677-1180c99bc583',
    'type': 1
    }


timeid_data={
    'barid': '53c2336a-5a67-4ca8-8677-1180c99bc583',
    'type': 1
    }

print('----结束')
kaiguan_url = 'https://test.wemew.cn/changeBaseGameState'
res4 = requests.request("POST", url=kaiguan_url, data=jiesu_data, headers=diannao_head)


print('开始')
kaiguan_url = 'https://test.wemew.cn/changeBaseGameState'
response1 = requests.request("POST", url=kaiguan_url, data=start_data, headers=diannao_head)

print('init')
init_url = 'https://test.wemew.cn/initDollMachine'
res2 = requests.request("POST", url=init_url, data=timeid_data, headers=diannao_head).json()
res2 = res2["resultMsg"]
res2 = json.loads(res2)
res2 = res2["gameId"]
print(res2)

print('手机请求')
shouji_url = 'http://test.wemew.cn/cwechat/payBaseGameForDollMachinetest?timeId='+res2
res3 = requests.request("GET", url=shouji_url, headers=shouji_head)
print(res3.text)



print('查数据库')
cursor.execute("select username,prizename,name,time   from base_game_result")
data = cursor.fetchall()
print(data)
time.sleep(60)



print('删数据')
time.sleep(20)
cursor.execute("DELETE from base_game_result ")


print('----结束')
kaiguan_url = 'https://test.wemew.cn/changeBaseGameState'
res4 = requests.request("POST", url=kaiguan_url, data=jiesu_data, headers=diannao_head)
print(res4.text)
#使用fetall()获取全部数据
data = cursor.fetchall()

#打印获取到的数据
print(data)