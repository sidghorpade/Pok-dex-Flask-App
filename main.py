# Title: main.py
# Description: Holds Flask application code and all routes to web pages

from ensurepip import version
from info import preprocess_evolution, preprocess_versions
import random
import pokebase as pb
import requests, json
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from pprint import pprint
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
@app.route('/info/<name>')
def info(name):
    pokemon = pb.pokemon(name)
    bio = pokemon.species.flavor_text_entries[0].__dict__['flavor_text']

    try:
        r = requests.get(pokemon.species.evolution_chain.url)
        data = r.json()
        evolution_dict = preprocess_evolution(data["chain"])
    except:
        print('error')

    gen_dict = preprocess_versions(pokemon.sprites.versions.__dict__, pokemon.id)

    return render_template('info.html', pokemon=pokemon, bio=bio, evolution_dict=evolution_dict, gen_dict=gen_dict)
  
# Lists Pokemon types
@app.route('/types')
def types():
    return render_template('types.html')
