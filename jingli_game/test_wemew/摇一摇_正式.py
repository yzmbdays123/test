from ws4py.client.threadedclient import WebSocketClient
from ws4py import websocket
import json, threading, time
import random
import xlrd


class Ws(WebSocketClient):

    def __init__(self, url, userId, user_icon, user_name):
        super().__init__(url)
        self.user_id = userId
        self.user_icon = user_icon
        self.user_name = user_name

    def opened(self):  # socket连接后调用
        req =json.dumps({"info":1,"barid":"82df6f95-55dd-43ab-a991-48833ff46a91","userid":self.user_id,"userhead":self.user_icon,"username":self.user_name})
        print(req)
        self.send(req)

    def closed(self, code, reason=None):
        print(code, time.strftime('%Y-%m-%d %H:%M:%S'))

    def received_message(self, message):
        resp = json.loads(str(message))
        print(resp)
        if resp.get('start') == 2:
            while True:
                req2 =json.dumps({'count':'1','userid':self.user_id,'num':0,'barid':'82df6f95-55dd-43ab-a991-48833ff46a91'})
                self.send(req2)
                time.sleep(random.randint(1,2))



def start(user_id,user_icom,user_name):

    ws = Ws('wss://game1.wemew.com:5443/websocket/shakegame/82df6f95-55dd-43ab-a991-48833ff46a91/%s'% user_id,user_id,user_icom,user_name)
    ws.connect()
    websocket.Heartbeat(ws).run()
    print('hihiiiiiii')
    ws.run_forever()


if __name__ == '__main__':
        with open(r'.\userinfo.txt','r',encoding='utf-8') as a:
            users=a.readlines()
            for user in users:
                user_info=str(user).split(',')
                user_id=user_info[0]
                user_icon=user_info[1]
                user_name=user_info[2].split('\n')[0]
                th = threading.Thread(target=start, args=(user_id,user_icon,user_name))  # 创建线程
                th.start()  # 启动线程
                time.sleep(1)



