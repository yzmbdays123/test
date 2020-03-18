host = 'https://test.wemew.cn'
barid = '53c2336a-5a67-4ca8-8677-1180c99bc583'
jiami_barid = '1165F4CDB486AAE7FA91BD302C131FBF43FFC1DEFD0E6D79A2DE498C324EFD3CDDEF1863B90F9D86'
cookie = '848EE53AF81A92DD2A221F8EA3C5403C6CD1A4D3EBC3E8D134A89AEE874DE244B632193C4BF63494'
zhifu_way = 1

get_timeid_url = '/fcwechat/getLotteryToReadyDrawData'
zhifu_url = '/fcwechat/payLuckyKoi'
jieguo_url = '/fcwechat/convertPayLuckyKoi'

headers = {
        'accept': "*/*",
        'x-requested-with': "XMLHttpRequest",
        'user-agent': "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36",
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'Cookie': 'T_USERID=%s'%cookie +';T_BARBASEID_NEW='+jiami_barid+';' 
            }

class config:
    def get_barid(self):
        return barid
    
    def get_headers(self):
        return headers
    
    def get_jiami_barid(self):
        return jiami_barid
    
    def get_host(self):
        return host
    
    def cookie(self):
        return cookie
    
    def zhifu_way(self):
        return zhifu_way
    
    def timeid_url(self):
        return host + get_timeid_url
       
    def zhifu_url(self):
        return host + zhifu_url
       
    def jieguo_url(self):
        return host + jieguo_url

    def get_timeid_data(self):
        data = {
        'barid':self.get_barid(),
        }
        return data

    def zhifu_data(self,timeid=''):
        data={
            'barid':self.get_barid(),
            'xttype':self.zhifu_way(),
            'timeId':timeid,
            }
        return data

    def get_result_data(self,resultid=''):
        data={
            'barid':self.get_barid(),
            'resultId':resultid
            }
        return data

if __name__ == '__main__':
        data = config()
        print(data.get_headers())
        print(data.get_result_data())
        print(data.get_timeid_data())
        print(data.timeid_url())
        import  requests
        from public.func import str_to_json
        def get_timeid():
            res = requests.request('post',url=data.timeid_url(),data=data.get_timeid_data(),headers=data.get_headers()).json()
            res = res["resultMsg"]
            res = res["timeId"]
            return res
        get_timeid()