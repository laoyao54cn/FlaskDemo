# -*- coding=utf8 -*-
from News import app
from News.model.NewsModel import NewsModel
from News.Business.NewsBusiness import NewBusiness
from flask import request, render_template, flash, abort, url_for, redirect, session, Flask, g


@app.route('/adddata',methods=['GET'])
def adddata():
    return render_template("adddata.html")


@app.route('/add', methods=['POST'])
def add_entry():
    news = request.form['News']
    nm = NewsModel(news, 0)
    nb = NewBusiness()
    i = nb.addnews(nm)

    return render_template("AddResult.html", result=i)
