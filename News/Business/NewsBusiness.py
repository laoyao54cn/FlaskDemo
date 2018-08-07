# -*- coding=utf8 -*-
import News.SQLHelper.SQLite3_helper
from News.model import NewsModel


class NewBusiness:
    def addnews(self, nm1):
        str_sql = "insert into newsinfo(NEWS,DEL) values('"+nm1.NEWS+"',"+str(nm1.DEL)+")"
        sh = News.SQLHelper.SQLite3_helper.SQLite3Helper()
        i = sh.insert(str_sql)
        return i


if __name__ == '__main__':
    nb = NewBusiness()
    nm = NewsModel.NewsModel('今天天气晴朗，气温36度', 0)
    i = nb.addnews(nm)
    if i == 1:
        print("Success.")
    else:
        print("Failed.")

