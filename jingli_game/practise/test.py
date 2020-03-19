import sys
import os
s=sys.path.append(os.path.dirname(os.path.dirname(__file__)))
print(sys.path)
# import os
# path = r'../core'
# for filename in os.listdir(path):
#     print(filename)
# li = os.listdir(path)
# li = sorted(li,key=lambda x:os.path.getmtime(os.path.join(path,x)))
# print(li)
import requests
import json
url1 = 'http://quotes.money.163.com/hs/realtimedata/service/plate.php?host=/hs/realtimedata/service/plate.php&page=0&query=TYPE:HANGYE&fields=RN,NAME,STOCK_COUNT,PE,LB,HSL,PERCENT,TURNOVER,VOLUME,PLATE_ID,TYPE_CODE,PRICE,UPNUM,DOWNNUM,MAXPERCENTSTOCK,MINPERCENTSTOCK&sort=PERCENT&order=desc&count=25&type=query&callback=callback_1932607065&req=0193'
url2 = 'http://quotes.money.163.com/hs/realtimedata/service/plate.php?host=/hs/realtimedata/service/plate.php&page=1&query=TYPE:HANGYE&fields=RN,NAME,STOCK_COUNT,PE,LB,HSL,PERCENT,TURNOVER,VOLUME,PLATE_ID,TYPE_CODE,PRICE,UPNUM,DOWNNUM,MAXPERCENTSTOCK,MINPERCENTSTOCK&sort=PERCENT&order=desc&count=25&type=query&callback=callback_1199610773&req=01954'
url3 = 'http://api.money.126.net/data/feed/0000001'
def bankuaizhangdie():
    url = [url1,url2]
    bankuai_name=[]
    bankuai_zhangfu=[]
    for i in url:
        res = requests.get(i).text
        res = res.split('(')[1].split(')')[0]
        res = json.loads(res)['list']

        for m in res:
            name = m['NAME']
            percent = m['PERCENT']
            bankuai_name.append(name)
            bankuai_zhangfu.append(percent)
        # for n in res:
        #     percent = n['PERCENT']
        #     bankuai_zhangfu.append(percent)
    hh = zip(bankuai_name,bankuai_zhangfu)
    result=[]
    for i in hh:
        result.append(i)
    print(result)
    return str(result)

def shangzheng():
    shangzhengzhishu_name = ['当前点数','上涨下跌点数','涨跌幅','最高点数','最低点数','成交额度']
    shangzhengzhishu = []
    res = requests.get(url3).text.split('(')[1].split(')')[0]
    res = json.loads(res)
    res = res['0000001']
    shangzhengzhishu.append(res['price'])
    shangzhengzhishu.append(res['updown'])
    shangzhengzhishu.append(res['percent'])
    shangzhengzhishu.append(res['high'])
    shangzhengzhishu.append(res['low'])
    shangzhengzhishu.append(str(res['turnover'])[0:4]+'亿元')
    aa = zip(shangzhengzhishu_name,shangzhengzhishu)
    result=[]
    for i in aa:
        result.append(i)
        print(result)
    return str(result)



from public.send_email import send_email
username = '1193723749@qq.com'
password = 'umeblcelhkajfjbi'
rec = '838214651@qq.com'
file = './test.mp4'
import time
from datetime import datetime
while True:
    # time_now = time.strftime("%H:%M:%S", time.localtime())
    now = datetime.now()
    hour = now.hour
    if hour in [9,10,11,13,14]:
        content = bankuaizhangdie() + "\n" +shangzheng()
        title = 'this is test title'
        m = send_email(username,password,rec,title,content,file)
        m.send_msg()
        print("hello")
        ss = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " 定时发送测试"
        print(ss)
        time.sleep(600)
    else:
        time.sleep(3598)


