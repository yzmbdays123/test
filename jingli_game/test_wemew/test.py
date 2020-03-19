import aiohttp
import asyncio
import time

def get_url():
    fp =open('aiohttp1.txt','r')
    fp = fp.readlines()
    url = []
    for i in fp:
        f = i.replace('\n','')
        url.append(f)
    return url
def get_cookie():
    fp = open('csfcookie.csv','r')
    fp = fp.readlines()
    cookie = []
    for i in fp:
        f = i.replace('\n','')
        cookie.append(f)

    return cookie
host = 'http://test.wemew.cn'
url = get_url()
cookie = get_cookie()
data = {
    'barId': '53c2336a-5a67-4ca8-8677-1180c99bc583'
    }
async def run():
    async with aiohttp.ClientSession() as session:
        for i in range(len(url)):
            ur = host  + url[i]
            async with session.post(url=ur,headers=headers,data=data) as resp:
                print(await resp.text())

tasks = []
loop = asyncio.get_event_loop()

start_time = time.time()

for i in range(1):
    headers = {
    'accept': "*/*",
    'x-requested-with': "XMLHttpRequest",
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'Cookie': 'T_USERID=%s'% cookie[i] +'; barbase_market=119DA5283BB46899B8E967F34AE21C0DFBEA86CA2C6A5FDD8F34A93A81FE3A5DD0652C688BF698BB; b_l_sid=9476CE4DB0945F9594BF9F268D3B96E5F63D8E5821762D04C19D0F9F2E95CF76A8BA5A5FA84F583D; T_BARBASEID_NEW=1165F4CDB486AAE7FA91BD302C131FBF43FFC1DEFD0E6D79A2DE498C324EFD3CDDEF1863B90F9D86; Hm_lvt_bbcfda495d9cf0463dc64c3b6b0c4187=1577344008,1577429154,1577530281,1577761589; admin_barbaseid=45BA56CECC6F4F7B512F2C95CB539587EE12986F2A9AFB08E8BC151A65FDAA237B994E823BF5F8F6; AU=4A52B01760B5DCC7C887DE76FC707951EDD8A8C74DBCE02784DE03C6F7867980687068DE71558A4545C51E730B8E83FB; TK=249A7FCC62E9C71C6CD9C32E13B11F298B15F44F3EE4045FA06FA2A3C4DAB4D6327A9D1594D3D08A; SCREENV=90EF110663569BF5DDACA6495ABD898D29B5E78D5EC0A2D07E8C86BDF2E5846A99D2DDB163B3214B; JSESSIONID=3282E9649081E9386B774F261AA18196'
    }
    tasks.append(run())

end_time = time.time()

loop.run_until_complete(asyncio.wait(tasks))

loop.close()


print("开始时间：",str(start_time))

print("结束时间：",str(end_time))

print("运行时间：",str(end_time - start_time))
