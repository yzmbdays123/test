import requests
import json
open('2.txt','w+',encoding='utf-8')


headers = {

   'Host': 'api.amemv.com',

   'Accept': '*/*',

   'Cookie': 'install_id=40337863888; login_flag=d6f29ec905af4bf1101199aa942c466f; odin_tt=a1e12dc3e4b92de77cccf6be1717377188f8aa7582f703c1391c8dc7d4a0df1b166119681af4277bd2cdc8aeb56000a7; sessionid=718df70f4e4964723cd1c8337c367b45; sid_guard=718df70f4e4964723cd1c8337c367b45%7C1534207148%7C5184000%7CSat%2C+13-Oct-2018+00%3A39%3A08+GMT; sid_tt=718df70f4e4964723cd1c8337c367b45; ttreq=1$ad10f98ec66ad6df5b86a7b1a613c77bb674236d; uid_tt=765536856bdc4f0f299b85dbc7338982',

   'User-Agent': 'Aweme/2.3.1 (iPhone; iOS 11.4.1; Scale/2.00)',

   'Accept-Language': 'zh-Hans-CN;q=1',

   'Accept-Encoding': 'br, gzip, deflate',

   'Connection': 'keep-alive'

}



def get_info(url):

   res = requests.get(url,headers=headers)

   json_data = json.loads(res.text)

   datas = json_data['aweme_list']

   for data in datas:

       desc = data['desc']

       download_url = data['video']['play_addr']['url_list'][0]

       print(desc,download_url)

       f.write(desc+','+download_url+' ')



def download_url(desc,url):

   global i

   res = requests.get(url)

   if len(desc) == 0:

       desc = str(i)

   f = open('สำฦต/'+desc+'.mp4','wb')

   f.write(res.content)

   i = i + 1


i = 1

fp = open('2.txt','r', encoding='utf-8')

for line in fp.readlines():

   desc = line.split(',')[0]

   url = line.split(',')[1].strip(' ')

   print(url)

   download_url(desc,url)