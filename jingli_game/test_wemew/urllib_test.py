import urllib3


re = urllib3.PoolManager()
res = re.request('GET','https://www.baidu.com')
print(res.data)