import string
import random
import time
'''
1 页面 输入框,提交 显示压缩网址
2. 数据结构:
    id
    原网址
    短网址
3. 逻辑
    首页展示
    post请求  参数  压缩  存储  返回
    页面展示
    动态URL路由 302跳转
'''

def get_key():
    s = string.ascii_letters+string.digits
    key = [i for i in s]
    random.shuffle(key)
    return key


def log(*args, **kwargs):
    format = '%H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    with open('log.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)


