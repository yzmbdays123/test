def upstairs(num):
    if num==1:
        return 1
    if num==2:
        return 2
    else:
        return upstairs(num-1)+upstairs(num-2)
num = input("请输入台阶级数:")
try:
    num = int(num)
    steps = upstairs(num) 
    print("一共有",steps,"种方法上台阶")
except Exception as e:
    print("不是数字")
import random
while True:
    a = random.randint(0,100)
    print(a)