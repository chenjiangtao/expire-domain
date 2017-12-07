# -*- coding: utf-8 -*-
import random
import chardet
import datetime

class RandomChar():
    """用于随机生成汉字"""

    @staticmethod
    def Unicode():
        val = random.randint(0x4E00, 0x5FCF)
        # val = random.randint(0x4E00, 0x9FCF)
        return unichr(val)

    @staticmethod
    def GB2312():
        head = random.randint(0xB0, 0xCF)
        body = random.randint(0xA, 0xF)
        tail = random.randint(0, 0xF)
        val = (head << 8) | (body << 4) | tail
        str = "%x" % val
        return str.decode('hex').decode('gb2312')

    @staticmethod
    def generate_file(nums):
        f = open('tmp.txt', 'a+')
        for i in range(nums):
            s = RandomChar.Unicode()
            f.write(s.encode('utf-8'))
            # print s
        f.close()
        print 'tmp.txt is ok',nums


    @staticmethod
    def generate_topic(nums):
        topic =''
        for i in range(nums):
            topic += RandomChar.Unicode()
        print 'topic is ok,words in',nums,topic
        return topic


    @staticmethod
    def generate_sensitive(nums):
        sensitive_list = [0]*nums

        for i in range(nums):
            s =''
            r = random.randint(1,5)
            for j in range(r):
                s += RandomChar.Unicode()
            sensitive_list[i]=s
        print '生成关键字:',len(sensitive_list),sensitive_list
        return sensitive_list


if __name__ == '__main__':
    # RandomChar.generate_file(100)
    sen = RandomChar.generate_sensitive(10000)
    topic =RandomChar.generate_topic(100000)

    starttime = datetime.datetime.now()
    i=1;
    for w in sen:
        s = topic.find(w)
        if s > 0:
            i=i+1
            # print s,w
    print '找到',i
    endtime = datetime.datetime.now()
    print (endtime - starttime).seconds,'秒'



