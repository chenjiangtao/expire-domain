#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import requests
from datetime import date

def connectdb():
    print('连接到mysql服务器...')
    # 打开数据库连接
    # 用户名:hp, 密码:Hp12345.,用户名和密码需要改成你自己的mysql用户名和密码，并且要创建数据库TESTDB，并在TESTDB数据库中创建好表Student
    db = MySQLdb.connect("localhost","root","yxpai8848","domain")
    print('连接上了!')
    return db

def querydb(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    #sql = "SELECT * FROM Student \
    #    WHERE Grade > '%d'" % (80)
    sql = "SELECT * FROM top"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()

        for row in results:
            ID = row[0]
            Name = row[1]
            # 打印结果
            print "ID: %s, Name: %s " % \
                (ID, Name,)
    except:
        print "Error: unable to fecth data"


def getTopSites(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    #sql = "SELECT * FROM Student \
    #    WHERE Grade > '%d'" % (80)
    sql = "SELECT SUBSTRING_INDEX(site,'.',1) FROM top"

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print '数据库读取100万数据成功'
        return results
    except:
        print "Error: unable to fecth data"

def closedb(db):
    db.close()

def getexpire(topSites):
    today = date.today()
    strDate=today.strftime("%Y/%m/%d")
    print strDate
    url = 'https://expire.biz/' + strDate
    print url
    # response = requests.get('https://expire.biz/2017/12/05')
    response = requests.get(url)
    print "response get sucess"
    contents = response.content
    tmplist = contents.split('\r\n')
    print strDate,"have",len(tmplist),"site expired,正在比对中。。。"
    sites =["one"]
    goodOne = ["one"]
    for site in tmplist:
        # print site
        siteName = site.split('.')[0]
        # print siteName
        if siteName in topSites:
            sites.append(site)
            if len(siteName) < 5:
                print site
                goodOne.append(site)

    print '------->>> 可能是好网站:',goodOne
    print '------->>> Top100万内的网站:',sites

def main():
    db = connectdb()  # 连接MySQL数据库
    topSites = getTopSites(db)
    # querydb(db)
    closedb(db)  # 关闭数据库
    getexpire(topSites)

if __name__ == '__main__':
        main()