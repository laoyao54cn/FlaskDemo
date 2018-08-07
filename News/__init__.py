# -*- coding: utf-8 -*-
from flask import Flask
# 创建项目对象
app = Flask(__name__)

from News.model.NewsModel import NewsModel
from News.Business.NewsBusiness import NewBusiness
from News.SQLHelper import SQLite3_helper
from News.controller import Newscontroller

