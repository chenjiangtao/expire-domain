#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import requests
from datetime import date


def connectdb():
    print('连接到mysql服务器...')
    # 打开数据库连接
    # 用户名:hp, 密码:Hp12345.,用户名和密码需要改成你自己的mysql用户名和密码，并且要创建数据库TESTDB，并在TESTDB数据库中创建好表Student
    # db = MySQLdb.connect("192.168.1.144","root","123456","whiteplante")
    db = MySQLdb.connect("localhost", "root", "yxpai8848", "domain")
    print('连接上了!')
    return db


def selectdb(db):
    cursor = db.cursor()
    sql = "SELECT * FROM test"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print "插入的数据有", len(results), results
    except:
        print "fetch 失败"


def insertdb(db):
    cursor = db.cursor()
    # insert_stmt = (
    #     "INSERT INTO `whiteplante`.`matter_doctor` (emp_no, first_name, last_name, hire_date) "
    #     "VALUES (%s, %s, %s, %s)"
    # )
    insert = (
        "INSERT INTO `domain`.`test`(`name`) "
        "VALUES (%s)"
    )
    try:
        for i in range(1000):
            # insert = "INSERT INTO `whiteplante`.`matter_doctor`(`id`, `key`, `puarentKey`, `score`, `pkey`, `update_time`, `doctor_id`) VALUES ("+i+", '1', '1', 4, '3', '2017-12-06 13:49:18', '1')"
            # 执行SQL语句
            data = [("中国人民")]
            # cursor.execute(insert, ('sss'))
            cursor.execute(insert, data)
            # 获取所有记录列表
        db.commit()
        print '数据插入完毕'
    except:
        db.rollback()
        print "Error: unable to insert data"


def closedb(db):
    db.close()


def main():
    db = connectdb()  # 连接MySQL数据库
    insertdb(db)
    selectdb(db)
    closedb(db)  # 关闭数据库


if __name__ == '__main__':
    main()
