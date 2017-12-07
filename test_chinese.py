#-*- coding:utf-8 -*-
import random

def check_contain_chinese(check_str):
    for ch in check_str.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

def iter_chinese():
    str =''
    for i in range(0x4e00,0x9fff):
        str+= unichr(i)
        print str,'\r'

    str=''
    for i in range(100):
        str+= unichr(random.randint(0x4E00, 0x9FCF))
    print str


if __name__ == "__main__":
    print check_contain_chinese('中国')
    print check_contain_chinese('xxx')
    print check_contain_chinese('xx中国')
    iter_chinese()



