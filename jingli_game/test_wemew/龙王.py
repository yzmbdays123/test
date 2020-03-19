import re
import requests
from bs4 import BeautifulSoup 

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'jieqiVisitId=article_articleviews%3D26975'
    }

def get_url():
    with open('lw.html','r') as f:
        fp = f.read()
    p1 = re.compile('26975/(.*?).html"')
    hh = re.findall(p1,fp)
    return hh

def get_con(id):
    html = requests.get('https://www.haotxt.com/xiaoshuo//26/26975/'+ id +'.html',headers=headers)
    html.encoding=html.apparent_encoding
    # html = html.encode("ISO-8859-1")
    # html = html.decode("utf-8")
    ss=html.text
    return ss
url = get_url()
url1=[]
for i in url:
    i = int(i)
    url1.append(i)
url1.sort()
w = open('d15.txt','a',encoding='utf-8')
for id in url1:
    id = str(id)
    ss = get_con(id)
    soup = BeautifulSoup(ss,'html.parser')
    title = soup.find(name='div',id="title").text
    content = soup.find(name='div',id="content").text
#     content.replace('\n','')
    print(title)
    w.write(title)
    w.write('\n')
    w.write(content)
    w.write('\n')
w.close()







