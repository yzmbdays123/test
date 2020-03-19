import os
import  requests
from public.send_email import send_email
username = '1193723749@qq.com'
password = 'umeblcelhkajfjbi'
rec = '838214651@qq.com'
file = './test.mp4'
content = '多情自古空余恨'
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = curPath[:curPath.find("myProject\\")+len("myProject\\")]  # 获取myProject，也就是项目的根路径
# dataPath = os.path.abspath(rootPath + 'data\\train.csv') # 获取tran.csv文件的路径
# print(curPath)
# print(rootPath)
# qq=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# print(qq)
aa=os.path.dirname(os.path.dirname(__file__))
print(aa)
# cc = os.path.dirname(__file__)
# print(cc)
# print(os.path.abspath(os.path.join(os.getcwd(), "../..")))
res = requests.get(url='https://www.cls.cn/telegraph',)
res = res.content
title = res.title()
res = res.decode()
# res = str(res)
print(res)
file = open('cls.html','w',encoding='utf-8')
file.write(res)
c = send_email(username=username,password=password,rec=rec,title=title,content='',file='cls.html')
c.send_file()
# print('-----------')
# print(os.path.abspath("."))   #当前目录的绝对路径
# print(os.path.abspath(r".."))  #上级目录的绝对路径
# print(os.path.abspath(r"D:\python_workshop\python6\revise\函数.py"))