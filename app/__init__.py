from flask import Flask
from flask_bootstrap import Bootstrap
import gmaps


app = Flask(__name__)

bootstrap = Bootstrap(app)
from app import routes
