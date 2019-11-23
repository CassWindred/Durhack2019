from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Katie'}
    return render_template('index.html', title='Map', user=user, map=True)

@app.route('/getPlaceInfo/<placeId>')
def getPlaceInfo(placeId):
    pass
