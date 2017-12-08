#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import requests
from datetime import date
import sys


def connectdb():
    print('连接到mysql服务器...')
    # 打开数据库连接
    # 用户名:hp, 密码:Hp12345.,用户名和密码需要改成你自己的mysql用户名和密码，并且要创建数据库TESTDB，并在TESTDB数据库中创建好表Student
    db = MySQLdb.connect("localhost", "root", "yxpai8848", "domain")
    print('连接上了!')
    return db


def querydb(tableName, db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    # sql = "SELECT * FROM Student \
    #    WHERE Grade > '%d'" % (80)
    sql = "SELECT * FROM `{}`".format(tableName)
    print sql
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()

        for row in results:
            site = row[0]
            desc = row[1]
            # 打印结果
            print "site: %s, desc: %s " % (site, desc)

        print "查得数据%s条" % len(results)
    except:
        print "Error: unable to fecth data"


def create_expired_table(tableName, db):
    cursor = db.cursor()
    sql = "CREATE TABLE `{}` (`site` varchar(20),`desc` varchar(20) " \
          "CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,PRIMARY KEY (`site`))" \
          " ENGINE=InnoDB DEFAULT CHARSET=utf8;".format(tableName)
    print sql

    try:
        cursor.execute(sql)
        print 'create table success:', tableName
        return True
    except:
        print 'create table failed:', tableName
        return False


def get_top_sites(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    # sql = "SELECT * FROM Student \
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


def get_expire_today():
    today = date.today()
    strDate = today.strftime("%Y/%m/%d")
    return strDate

#
# def get_tablename_today():
#     today = date.today()
#     strDate = today.strftime("%Y%m%d")
#     return strDate


def insert_site(site, desc, db, tableName):
    cursor = db.cursor()
    sql = "INSERT INTO `domain`.`{}`(`site`, `desc`) VALUES ('{}', '{}')".format(tableName, site, desc)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print 'insert site failed \n', sql


def fetch_expired_site(topSites, strDate, db):
    url = 'https://expire.biz/' + strDate
    print '正在读取', url
    response = requests.get(url)
    print "读取成功"
    contents = response.content
    tmplist = contents.split('\r\n')
    print strDate, "have", len(tmplist), "site expired,正在比对中。。。"

    for site in tmplist:
        siteName = site.split('.')[0]
        if siteName in topSites:
            insert_site(site, 'top100M', db, strDate)
            print 'top 100M', site
        if len(siteName) < 5:
            insert_site(site, 'good', db, strDate)
            # print '.',
            # sys.stdout.write('.')


if __name__ == '__main__':
    db = connectdb()  # 连接MySQL数据库

    # 指定日期
    d = get_expire_today()
    # d = '2017/12/06'
    is_created = create_expired_table(d, db)
    if is_created:
        topSites = get_top_sites(db)
        fetch_expired_site(topSites, d, db)

    querydb(d, db)

    closedb(db)  # 关闭数据库
