import time
import websocket
# ws = websocket.WebSocket()
# ws.connect("wss://game2.wemew.com:1443/websocket/moneygame/53c2336a-5a67-4ca8-8677-1180c99bc583/", http_proxy_host="game2.wemew.com", http_proxy_port=1443)
# test=['7974379d-5dcb-46bb-8f97-f721379507df','09e-d7b9-4041-8561-93a847478b60','d8c2509e-d7b9-4041-8561-93a847478b60','0b5f406b-b765-4bc3-b596-032f60bea504',
# '16b5ec43-3fc5-4e86-b3ea-eabf14f4301c','bbcc55cd-41a0-416a-820b-f6442d70c972','be73ead8-5829-49b5-945f-ab4f14d1d16e','0d80c2ee-c461-41d8-bae0-ac7ea112c955'
# ]
ls=0
with open('youxi.txt','r',encoding='utf-8') as fr:
    lis = fr.readlines()

with open('user.txt','r',encoding='utf-8') as fp:
    user = fp.readlines()
print(lis[1])
print(user[1])
url1 = 'wss://game2.wemew.com:1443/websocket/moneygame/53c2336a-5a67-4ca8-8677-1180c99bc583/0b5f406b-b765-4bc3-b596-032f60bea504'


ws=websocket.WebSocket()
ws.connect(url=url1)
if ws.connected:

    time.sleep(1)
    for i in range(100):
        ws.send("moneyNum<>53c2336a-5a67-4ca8-8677-1180c99bc583<>0b5f406b-b765-4bc3-b596-032f60bea504<>10000")
        print(ws.recv())
        time.sleep(2)
    #关闭连接 
    ws.close()
    time.sleep(2)
