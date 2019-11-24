from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, SubmitInfoForm, SignUpForm
import database_manager

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = SubmitInfoForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('submit.html', title='Submit', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
    form = SignUpForm()
    if form.validate_on_submit():
        flash('Signup requested for user {}'.format(
            form.firstName.data))
        return redirect(url_for('index'))
    return render_template('signUp.html', title='Sign Up', form=form)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Katie'}
    return render_template('index.html', title='Map', user=user, map=True)

@app.route('/getPlaceInfo/<placeId>')
def getPlaceInfo(placeId):
    database_manager.place_access(placeId)


