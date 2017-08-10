from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Mitsui'}
    posts = [{'author':{'nickname':'John'},
              'body':'Beautiful day in Portland!'},
             {
                 'author':{'nickname':'Susan'},
                 'body':'今天是个好天气！！'
             }]

    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

