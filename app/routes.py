from app import app
from database_manager import *
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, SubmitInfoForm, SignUpForm
#import database_manager

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    user = getUser()
    form = SubmitInfoForm()
    if form.validate_on_submit():
        flash('submit request {}'.format(
            form.ID.data))
        if new_location(form.location.data, form.accessCategory.data, user) != False:
            return redirect(url_for('index'))
        else:
            return redirect(url_for('submit'))
        if add_rating(form.location.data, form.accessCategory.data, user, form.rating.data) != False:
                return redirect(url_for('index'))
        else:
            return redirect(url_for('submit'))
        if new_comment(form.location.data, form.accessCategory.data, user, form.comments.data) != False:
                return redirect(url_for('index'))
        else:
            return redirect(url_for('submit'))
    return render_template('submit.html', title='Submit', form=form, user=user)

@app.route('/submit/<placeId>', methods=['GET', 'POST'])
def submitPlace(placeId):
    user = getUser()
    form = SubmitInfoForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('submit.html', title='Submit', form=form, user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data))
        if check_if_password_is_correct(form.username.data, form.password.data): 
            logs = open("logs.txt", "w")
            logs.write(form.username.data)
            logs.close()
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
    form = SignUpForm()
    if form.validate_on_submit():
        flash('Signup requested for user {}'.format(
            form.firstName.data))
        if new_user(form.username.data, form.password.data, form.firstName.data, form.lastName.data) != False:
            return redirect(url_for('index'))
        else:
            return redirect(url_for('signUp'))
    return render_template('signUp.html', title='Sign Up', form=form)

@app.route('/')
@app.route('/index')
def index():
    user = getUser()
    return render_template('index.html', title='Map', user=user, map=True)

@app.route('/getPlaceInfo/<placeId>') #dont break it if there's no data!
def getPlaceInfo(placeId):
    try:
        logs = open("logs.txt", "r")
        user = logs.read()
        logs.close()
    except:
        return redirect(url_for('login'))
    new_location(placeId, "Light level", user)
    access_info = get_ratings(placeId)
    infoBoxContent=""
    for info in access_info:
        infoBoxContent += f"{info['Access Type']}: Rated {info['Average Rating']} by {info['Number of Ratings']} users. \n"

    return infoBoxContent

def getUser():
    try:
        logs = open("logs.txt", "r")
        user = logs.read()
        logs.close()
    except:
        user = ""
    return user


