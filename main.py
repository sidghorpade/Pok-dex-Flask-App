# Title: main.py
# Description: Holds Flaks application code and all routes to web pages

import random
import pokebase as pb
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from PIL import Image

# creating flask appliation
app = Flask(__name__)

# passing app to bootstrap
bootstrap = Bootstrap5(app)

# Homepage
@app.route('/')
def home():
    return render_template('home.html')

# Worked on by: Pedro
# Pokemon info route
@app.route('/info')
def info():
    return render_template('info.html')
  
# Lists Pokemon types
@app.route('/types')
def types():
    return render_template('types.html')
