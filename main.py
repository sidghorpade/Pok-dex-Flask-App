from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from PIL import Image
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/types')
def types():
    return render_template('types.html')
