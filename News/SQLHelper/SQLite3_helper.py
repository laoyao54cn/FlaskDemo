# -*- coding=utf8 -*-
import sqlite3
import os


class SQLite3Helper:
    __db = ''

    def __init__(self):
        str_path = os.path.dirname(os.path.realpath(__file__))+os.path.sep+".."
        self.__db = str_path + "/DB/info.db"
        self.con = sqlite3.connect(self.__db)
        self.cur = self.con.cursor()

    def insert(self, sql):
        self.cur.execute(sql)
        self.con.commit()
        return 1

    def __del__(self):
        self.cur.close()
        self.con.close()


if __name__ == '__main__':
    sh = SQLite3Helper()
    str_sql = "insert into newsinfo(NEWS,DEL) values('中文信息数据存储及显示',0)"
    i = sh.insert(str_sql)
    if i == 1:
        print("Success.")
    else:
        print("Failed.")

