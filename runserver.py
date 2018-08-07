from News import app
from flask import session
import os

@app.route('/')
def hello_world():
    session['username'] = 'Aming'
    return '<html><head><title>main page</title></head><body><a href="/News/adddata">添加新闻数据</a></body></html>'


# app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.secret_key = os.urandom(24)

if __name__ == '__main__':
    app.run(debug=True)
