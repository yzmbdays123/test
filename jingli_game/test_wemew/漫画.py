import re
import requests
from bs4 import BeautifulSoup 
from fileinput import filename

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cookie': 'PHPSESSID=10umpmsfnf32qcfcmed0c8ta72; Hm_lvt_ecb3501bb595c7329991bac49358921a=1578833673; UM_distinctid=16f99d1f9734e3-06babfedacc037-c383f64-1fa400-16f99d1f974b01; CNZZDATA1272815512=338166673-1578830842-%7C1578830842; Hm_lpvt_ecb3501bb595c7329991bac49358921a=1578835560'
    }

p1 = re.compile('16839/(.*?).html"')
def get_url():
    with open('mh.html','r',encoding='utf-8') as f:
        fp = f.read()
    hh = re.findall(p1,fp)
    return hh


def get_con(id):
    html = requests.get('https://m.bnmanhua.com/comic/16839/'+ id +'.html',headers=headers)
    html.encoding=html.apparent_encoding
    ss=html.text
    return ss

p2 = re.compile(r"16839(.*?).jpg")
p3 = re.compile('斗罗大陆4终极斗罗漫画-(.*?)-全')
def get_img(tx):
    imgurl = re.findall(p2, tx)
    return imgurl
  
def get_title(tx):
    title = re.findall(p3,tx)
    return title

url = get_url()
# com = get_con(url[2])
# i = get_img(com)
print(len(url))
print(url[63])
# o=i[1]
# print(type(o))
import time
for j in range(64,len(url)):
    con = get_con(url[j])
    img = get_img(con)
    print(img)
    for i in range(len(img)):
        img[i].replace('\\','')
        url='https://img.yaoyaoliao.com/upload/files/16839'+img[i]+'.jpg'
        q=url.split('\\')
        url = q[0]+q[1]+q[2]
        res = requests.get(url=url)
        title = get_title(con)
        time.sleep(0.1)
        filename = 'D:\\HH\\%s_%s.jpg' % (title,str(i))
        w = open(filename,'wb')
        w.write(res.content)
         
        
# url1.sort()
# w = open('d6.txt','a',encoding='utf-8')
# for id in url1:
#     id = str(id)
#     ss = get_con(id)
#     soup = BeautifulSoup(ss,'html.parser')
#     title = soup.find(name='div',id="title").text
#     content = soup.find(name='div',id="content").text
#     print(title)
#     wr=w.write(title)
#     w.write('\n')
#     wr=w.write(content)
#     w.write('\n')
# w.close()
