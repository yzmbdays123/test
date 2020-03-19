import aiohttp
import asyncio
import time
start_time = time.time()

async def run():
    async with aiohttp.ClientSession() as session:
        ur = 'https://www.baidu.com'
        async with session.post(url=ur) as resp:
            print(resp.status)
                
                
tasks = []
tasks1 = []
loop = asyncio.get_event_loop()
for i in range(400):

    tasks.append(run())
    print(i)

loop.run_until_complete(asyncio.wait(tasks))

loop.close()
time.sleep(3)
print('........................')
loop1 = asyncio.get_event_loop()
for i in range(300):

    tasks1.append(run())
    print(i)

loop.run_until_complete(asyncio.wait(tasks1))

loop1.close()
end_time = time.time()

print("开始时间：",str(start_time))

print("结束时间：",str(end_time))

print("运行时间：",str(end_time - start_time))