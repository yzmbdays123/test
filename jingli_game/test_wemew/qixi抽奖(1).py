import requests
import json
import time
url = "https://weixin.wemew.com/cwechat/payDice"
url1 = "https://weixin.wemew.com/cwechat/pollingDice"
url2 = "https://weixin.wemew.com/cwechat/diceRanking"

payload1 = {
'timeId':'c04a33cf1ab44560af9add6a168053a0','table':' ','number':'1'}
headers = {
    'accept': "*/*",
    'x-requested-with': "XMLHttpRequest",
    'user-agent': "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36",
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'Cookie':'C_USERID_NEW=E3D5ACCB01A55D7BCB5C758FC5ED2BF1EF6805D122FA5C2803D61859C29A44825B599A499AE7DB6B; T_BARBASEID=AF3C19EDADF726C73EE7471BB8257D4681BE15EBE031F94C0286F9B65E0A04F5FF7786F4F9B26872',
}
headers2 = {
    'accept': "*/*",
    'x-requested-with': "XMLHttpRequest",
    'user-agent': "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36",
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'Cookie': 'Hm_lpvt_bbcfda495d9cf0463dc64c3b6b0c4187=1569375963; Hm_lvt_bbcfda495d9cf0463dc64c3b6b0c4187=1568872048,1569202826,1569240389,1569375963; T_USERID=055D81D8600F188457FF3862C962059CBAB29548ED2DFF644B773BF40DEA57DD987B427948DF7B28; T_USERID=055D81D8600F188457FF3862C962059CBAB29548ED2DFF644B773BF40DEA57DD987B427948DF7B28; admin_barbaseid=1165F4CDB486AAE7FA91BD302C131FBF43FFC1DEFD0E6D79A2DE498C324EFD3CDDEF1863B90F9D86; AU=4A52B01760B5DCC7C887DE76FC707951EDD8A8C74DBCE02784DE03C6F7867980852AE7594871BFCC1FBA94F2A4BC23BD; b_l_sid=102089370CF1E544017795E9B5A190E86A5FE6DDEE745AF43557C3BED4FD84F753060C3BBBA2EC38; barbase_market=EF0EB817A2A15CE6FE5CDFA61E1C0CB2399D41401B49AC970CBBE8149B366F211ADD16A55ECAFE50; JSESSIONID=30DE646CE0C2629A4EB573AEE8393005; SCREENV=9ABF513678239B98320056C84D7CF8E39529B4F170ED4670CC2F07CA044F02E8E41A2E6A9773AF56; T_BARBASEID_NEW=1165F4CDB486AAE7FA91BD302C131FBF43FFC1DEFD0E6D79A2DE498C324EFD3CDDEF1863B90F9D86'  }

def testnum(string):
    str_len = len(string)
    res = 0
    for i in range(str_len):
        res += int(string[i])
    return res
i=0
while i<80:
    response = requests.request("POST", url, data=payload1, headers=headers).json()["resultMsg"]
    resid=json.loads(response)["resultId"]
    payload2 = {
    'resultId': resid
      }
    response1 = requests.request("POST", url1,data=payload2, headers=headers)
    
    response2 = requests.request("POST", url2,data=payload2, headers=headers)
    

    res2=response2.json()['resultMsg']
    resnum=json.loads(res2)

    num = resnum['obj']['animals']
    num=json.loads(num)
    num=num['num']
    a=testnum(num)
    print(i,'----->>>>',num,a)
    i+=1
    time.sleep(3)


