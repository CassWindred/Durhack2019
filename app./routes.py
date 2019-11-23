from app import app

from flask import render_template


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    user = {'username': 'Katie'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/')
def hello_world():
    user = {'username': 'Katie'}
    return render_template('index.html', user=user)
