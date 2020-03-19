from websocket import create_connection
import time
from threading import Thread
with open('888.txt','r',encoding = 'utf-8') as f:
    fp = f.read().split('\n')
print(fp)
with open('77.txt','r',encoding = 'utf-8') as fd:
    user = fd.read().split('\n')
print(user)

def ws(wsurl,info):
    ws = create_connection(wsurl)
    ws.send(info)
time.sleep(1)
for i in range(len(fp)):
    wsurl = 'wss://game1.wemew.com:2443/websocket/horsegame/cd3ea31f-ab5e-4db7-866f-8f6b0826cded/' + user[i]
    t = Thread(target=ws,args=(wsurl,fp[i]))
    t.start()
    t.join()
    time.sleep(0.5)
    
# while True:
#     result =  ws.recv()
#     print("Received '%s'" % result)
#     time.sleep(5)
ws.close()