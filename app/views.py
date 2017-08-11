from app import app
from flask import render_template,flash,redirect
from .forms import LoginForm

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


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                           title = 'Sign In',
                           form = form)