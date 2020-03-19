
import psutil


cpu=(str)(psutil.cpu_percent(1))+'%'
print(cpu)
p1=psutil.Process(10140)  # 进程4420占用的CPU
p2=psutil.Process(21876)
print(p1,p2)
for x in range(100):
    x1=p1.cpu_percent(1)
    x2=p2.cpu_percent(1)
    print(x1,x2)
    print(cpu)