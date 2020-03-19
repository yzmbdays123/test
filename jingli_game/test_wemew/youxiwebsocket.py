import websocket

import json
import _thread
import time

url = "wss://game2.wemew.com:1443/websocket/moneygame/53c2336a-5a67-4ca8-8677-1180c99bc583/"   # 接口地址

def on_message(ws, message):
   print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("close connection")

def on_open(ws):
    def run(*args):
        content = 'moneyNum<>53c2336a-5a67-4ca8-8677-1180c99bc583<>0b5f406b-b765-4bc3-b596-032f60bea504<>10'
        ws.send(content)
        

        time.sleep(1.5)
        ws.close()
    _thread.start_new_thread(run, ())

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

    