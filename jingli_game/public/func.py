import json
import os


def str_to_json(string):
    try:
        st = json.loads(string)
        return st
    except:
        print('字符串转换json不成功')

# 写入csv
def write_csv(s):
    with open('jieguo.csv','a',encoding='utf-8') as f:
        f.write(s+'\n')
        f.close()

#获取文件夹下面的文件，并按时间顺序排列
def get_file_name(path):
    li = os.listdir(path)
    li = sorted(li,key=lambda x:os.path.getmtime(os.path.join(path,x)))
    return li
