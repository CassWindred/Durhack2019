from flask import Flask
from flask_bootstrap import Bootstrap
from flask_googlemaps import GoogleMaps as gmaps

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
