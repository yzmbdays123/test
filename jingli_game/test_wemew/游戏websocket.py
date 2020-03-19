import websocket

import time

import threading

import gzip

#import json

#from threadpool import ThreadPool, makeRequests

#from websocket import create_connection

url = "wss://game2.wemew.com:1443/websocket/moneygame/53c2336a-5a67-4ca8-8677-1180c99bc583/"
ws = websocket.create_connection(url)

#SERVER_URL = "wss://i.cg.net/wi/ws"

#SERVER_URL = "wss://www.exshell.com/r1/main/ws"

def on_message(ws, message):

    print(message)

 

def on_error(ws, error):

    print(error)

 

def on_close(ws):

    print("### closed ###")

 

def on_open(ws):

    def send_trhead():

 

        send_info = '{"sub": "market.ethusdt.kline.1min","id": "id10"}'

        #send_info = '{"event":"subscribe", "channel":"btc_usdt.deep"}'

        while True:

            #time.sleep(5)

            #ws.send(json.dumps(send_info))

            ws.send(send_info)

            while (1):

                compressData = ws.recv()

                result = gzip.decompress(compressData).decode('utf-8')

                if result[:7] == '{"ping"':

                    ts = result[8:21]

                    pong = '{"pong":' + ts + '}'

                    ws.send(pong)

                    ws.send(send_info)

                else:

                    #print(result)

                    with open('./test_result.txt', 'a') as f:

                        f.write(threading.currentThread().name+'\n')

                        f.write(result+'\n')

 

    t = threading.Thread(target=send_trhead)

    t.start()

    print(threading.currentThread().name)

def on_start(a):

 

    # time.sleep(2)

    # websocket.enableTrace(True)

    # ws = websocket.WebSocketApp(SERVER_URL,

    #                             on_message=on_message,

    #                             on_error=on_error,

    #                             on_close=on_close)

    # ws.on_open = on_open

    # ws.run_forever()

    #print(a[2])

    try:

        ws = websocket.create_connection(SERVER_URL)

        on_open(ws)

    except Exception as e:

        print('error is :',e)

        print('connect ws error,retry...')

        time.sleep(5)

if __name__ == "__main__":

 

    # pool = ThreadPool(3)

    # test = list()

    # for ir in range(3):

    #     test.append(ir)

    #

    # requests = makeRequests(on_start, test)

    # [pool.putRequest(req) for req in requests]

    # pool.wait()

    # # #on_start(1)

 

    for ir in range(20):

        on_start(1)

        time.sleep(0.1)