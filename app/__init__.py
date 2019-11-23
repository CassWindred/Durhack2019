from flask import Flask
from flask_bootstrap import Bootstrap
from flaskext.googlemaps import GoogleMaps as gmaps

app = Flask(__name__)

bootstrap = Bootstrap(app)
gmaps(app)
from app import routes
