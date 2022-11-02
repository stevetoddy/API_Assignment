from flask import Flask
from init import db, ma
import os

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world'

