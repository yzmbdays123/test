import requests
import time
import random

data_typy = [9,23,176,35,66,72,87,76,17,73,175,173,169,0,24,21,2,68,168,1,161,65,37,3,5,172,75,91,82,30]
dashang_id = [118,116,114,113,110,109,107,105,104,103,102,101,94,15,93,89,72,97,83,91,81,75,73,70,59,33,25,24,19,18,17,38]
url_img = ['https://wemew.oss-cn-qingdao.aliyuncs.com/2019-12-10-10/157594399423290450.jpg?x-oss-process=style/100','https://wemew.oss-cn-qingdao.aliyuncs.com/2019-12-10-10/157594401551505181.jpg?x-oss-process=style/100','https://wemew.oss-cn-qingdao.aliyuncs.com/2019-12-10-10/157594399949181726.jpg?x-oss-process=style/100','https://wemew.oss-cn-qingdao.aliyuncs.com/2019-12-10-10/157594396407515233.jpg?x-oss-process=style/400']
headers = {
    'Cookie':'C_USERID_NEW=E3D5ACCB01A55D7BCB5C758FC5ED2BF1EF6805D122FA5C2803D61859C29A44825B599A499AE7DB6B; __jsluid_h=e9b4368ecd0fda78f88eba0b6f9f7e48; __jsluid_s=70fa4101ca4ddea9ae03cabd9ff54838; T_BARBASEID=AF3C19EDADF726C73EE7471BB8257D4681BE15EBE031F94C0286F9B65E0A04F5FF7786F4F9B26872; Hm_lvt_bbcfda495d9cf0463dc64c3b6b0c4187=1575615982,1575623540,1575625747,1575875408; JSESSIONID=D0FC25F1AF618BF882F68161DE8FD2D5; Hm_lpvt_bbcfda495d9cf0463dc64c3b6b0c4187=1575877954',
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    }
url = 'https://weixin.wemew.com/cwechat/pascreenPay'
url1 = 'https://weixin.wemew.com/cwechat/newPlayTheShowPay'
def data(string='',das=''):
    bap_data = {
        'sitnum': '',
        'second': 30,
        'msg': '啤酒骰子来一手，洋酒红酒喝起走',
        'img': 'https://wemew.oss-cn-qingdao.aliyuncs.com/2019-12-10-10/157594399949181726.jpg',
        'msgid': '',
        'showNum': 1,
        'videoUrl': '',
        'xttype': 3,
        'seatNumber': '',
        'cigarettePrice': -1,
        'usePascreenExperience': 'false',
        'isDoubleOne': 0,
        'isCheckVip': 'false',
        'btnNum': '',
        'theme': string,
        'isMiniApp': 'false'
        }
    das_data = {
        'pid': '1f676da1-8bae-4af1-b14d-d56549fdcf41',
        'flower': das,
        'txt': 'ACXASX',
        'userId': '',
        'isShowToPc': 'true',
        'xttype': 3,
        'source': 3,
        'showNum': 1,
        'dsSource': 1,
        'isMiniApp': 'false',
    }
    if string == '':
        return das_data
    else:
        return bap_data

for i in range(0,len(dashang_id)):
    num = random.randint(0,1)
    if num == 1:
        das_data =data(string=data_typy[i],das='')
        url_t = url
    else:
        das_data = data(string='',das=dashang_id[i])
        url_t = url1
    res = requests.post(url=url_t,data=das_data,headers=headers)
    print(i,'  >>>>  ',res.text)
    time.sleep(30)


#
# for i in range(20,len(data_typy)):
#     num = random.randint(0,3)
#     bap_data = data(data_typy[i])
#     res = requests.post(url=url,data=bap_data,headers=headers)
#     print(i,'  >>>>  ',res.text)
#     time.sleep(30)


    



