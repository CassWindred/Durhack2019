from app import app

from flask import render_template


@app.route('/example')
def example():
    return "This is an example page!"


@app.route('/')
def hello_world():
    user = {'username': 'Miguel'}
    return render_template('mainpage.html', title='Home', user=user)

@app.route('/getPlaceInfo/<placeId>')
def getPlaceInfo(placeId):
    pass
