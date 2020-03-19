import requests
import json
import time

url = "http://test.wemew.cn/cwechat/pascreenPay"
url1 = "http://test.wemew.cn/cwechat/whiteDayLastUserGift"
url2 = 'https://test.wemew.cn/cwechat/whiteDayGrabBagRain'
url3 = 'https://test.wemew.cn/cwechat/buyMountV2'


a= open(r'test_user_id_encrypt.csv','r') 
#     d = csv.reader(a)
b = a.readlines()

# 买头饰
data={
    'pid': '853bb63b2352425bad046dd4b589b59a',
    'xttype': 1,
    'num': 3
    }

# 霸屏
payload = {
    'sitnum': '',
    'second': 6,
    'msg': '一夜辗转五六场，扶墙赶往下一场',
    'img': '',
    'msgid':'' ,
    'showNum': 1,
    'videoUrl': '',
    'xttype': 2,
    'seatNumber':'' ,
    'cigarettePrice': -1,
    'usePascreenExperience': 'false',
    'isDoubleOne': 0,
    'isCheckVip': 'false',
    'btnNum':'' ,
    'isMiniApp': 'false',
    
    }
def shidian():
    m=0
    for j in range(500):
        c=b[j].replace('\n','')
        headers = {
        'accept': "*/*",
        'x-requested-with': "XMLHttpRequest",
        'user-agent': "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36",
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'Cookie': 'T_USERID=%s'%c +';T_BARBASEID_NEW=1165F4CDB486AAE7FA91BD302C131FBF43FFC1DEFD0E6D79A2DE498C324EFD3CDDEF1863B90F9D86;' 
            }
    #     response = requests.request("POST", url, data=payload, headers=headers)
    #     response1 = requests.request("POST", url1, headers=headers).json()
        response3 = requests.request("POST", url2, headers=headers).text
    
        
        print(response3)
        m+=1
        print(m)
        time.sleep(3)
        
#  C1BCAA0052EF7151F52851D036C343E5C1F24B1A183477EED259601CFC22E0D9C92978AFFE27083A;' 
#1165F4CDB486AAE7FA91BD302C131FBF43FFC1DEFD0E6D79A2DE498C324EFD3CDDEF1863B90F9D86;' 
def bapingchoujiang(x,m):
    n=0
    yic=0
#     wuer=0
#     ba=0
#     wu=0
#     san=0
#     er=0
#     yi=0
#     ling=0
#     toushiheyanshiquan=0
#     erling=0
#     fen=0
#     toushi=0
#     yanshiquan=0
    for j in range(x,m):
        c=b[j].replace('\n','')
        headers = {
        'accept': "*/*",
        'x-requested-with': "XMLHttpRequest",
        'user-agent': "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36",
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'Cookie': 'T_USERID=%s'%c +';T_BARBASEID_NEW=C1BCAA0052EF7151F52851D036C343E5C1F24B1A183477EED259601CFC22E0D9C92978AFFE27083A;' 
            }
        response = requests.request("POST", url3, data=data, headers=headers,)
        response1 = requests.request("POST", url1, headers=headers)
        try:
            res=response1.json()
            res = res['resultMsg']
            res = json.loads(res)
            res = res['giftName']
            print(res)
           
        except:
            print('异常',response1.text)
            print('总次数：',n)
            yic+=1
#             print(ba,wu,san,er,yi,ling,fen,erling,yanshiquan,toushi)
        n+=1
        
    #     print(response1)
    #     print(res)
        time.sleep(1)
    print('总次数：',n,'异常',yic)

bapingchoujiang()
if __name__ == '__main__':
    import threading
    t1 = threading.Thread(target=bapingchoujiang, args=(0,250))
    t2 = threading.Thread(target=bapingchoujiang, args=(250,500))
    t3 = threading.Thread(target=bapingchoujiang, args=(500,750))
    t4 = threading.Thread(target=bapingchoujiang, args=(750,1000))
 
    t3.start()
    t4.start()

#shidian()