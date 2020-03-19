import requests
import json

import time

# def getGameId(url,data):
#     res = requests.post(url=url,data=data)
#     return 'ok'



url = "http://192.168.5.29/test1/payBaseGameForDollMachine"

data = {
        'timeId':'c8bc1f65e8ed4fe8b93dab4f35cc9a32'
    }


i = 0
while i<5000:
    res = requests.post(url=url,data=data)
    i+=1
    print(i)
    