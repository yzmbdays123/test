import requests
import json
import time
import random
# def getGameId(url,data):
#     res = requests.post(url=url,data=data)
#     return 'ok'
# url1 = "http://192.168.5.29/test1/payBaseGameForDollMachine"

def re_data():
    userid = random.randint(1,15)
    userid = str(userid)
    data = {
            'userid':2,
            'timeId':'8159382cefee40a9b6fedcaa61590c15'
        }
    return data

headers = {
    'Cookie': 'SCREENV=212C998EBC3D0C0D49C89F8ACEC56182B0934D9FB535B19F48EA77E70A7B6E6B7D86092B07E64E0A; Hm_lvt_bbcfda495d9cf0463dc64c3b6b0c4187=1577261227; JSESSIONID=E1D464DFFB6523684EC37CF3C5D56B83; admin_barbaseid=1FC9F878AEDFEAA8B329D719E4AD244FD2E971577EA8B055291CB5C2A5ED1A49ED0247ED75015603; AU=4A52B01760B5DCC7C887DE76FC707951EDD8A8C74DBCE02784DE03C6F7867980C5C3EF2AC9E504A8275446661644AAB3; Hm_lpvt_bbcfda495d9cf0463dc64c3b6b0c4187=1577347027; C_USERID_NEW=8496EB110FEF27F0',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
url2 = 'http://192.168.5.29/cwechat/payBaseGameForDollMachine'
i = 0

while i<200:
    data = re_data()
    res = requests.post(url=url2,data=data,headers=headers)
    i+=1
    time.sleep(0.2)
    print(i,data['userid'],res.text)
    