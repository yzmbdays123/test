from websocket import create_connection
import time
import random
def ws(wsurl,info):
    ws = create_connection(wsurl)
    ws.send(info)
    time.sleep(5)
    ws.send(inf)
wsurl = 'wss://game1.wemew.com:5443/websocket/shakegame/53c2336a-5a67-4ca8-8677-1180c99bc583/2100a6ac-649c-4ba9-bdfc-bac6c19a0ed1'
info = {
   
'barid': "53c2336a-5a67-4ca8-8677-1180c99bc583",
'info': "1",
'userhead': "https://wemew.oss-cn-qingdao.aliyuncs.com/2019-12-05-16/157553306489590614.jpg",
'userid': "2100a6ac-649c-4ba9-bdfc-bac6c19a0ed1",
'username': "微苗"
    }

inf = req2 =str({'count':"1",'userid':'2100a6ac-649c-4ba9-bdfc-bac6c19a0ed1','num':random.randint(100,200),'barid':'53c2336a-5a67-4ca8-8677-1180c99bc583'})
info = str(info)
while 1:
    ws(wsurl,info)

