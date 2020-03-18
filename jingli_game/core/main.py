import requests
import json
import time
from public.func import *

from config.config import config
data = config()

def get_timeid():
    res = requests.post(url=data.timeid_url(),data=data.get_timeid_data(),headers=data.get_headers()).json()
    res = res["resultMsg"]
    res = res["timeId"]
    return res
timeid=get_timeid()

def get_resultid():
    res = requests.post(url=data.zhifu_url(),data=data.zhifu_data(timeid),headers=data.get_headers()).json()
    res = res["resultMsg"]
    res = res["resultId"]
    print(res)
    return res
def look_jieguo(result):
    res = requests.post(url=data.jieguo_url(),data=data.get_result_data(result),headers=data.get_headers()).json()
    res = res['resultMsg']
    res = str_to_json(res)
    res = res['name']
    return res
for i in range(10):
    result=get_resultid()
    write_csv(look_jieguo(result))
    time.sleep(3)

