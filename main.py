# Title: main.py
# Description: Holds Flask application code and all routes to web pages

from ensurepip import version
from info import preprocess_evolution, preprocess_versions, preprocess_stats, preprocess_habitats
from transformations import transform_image
import random
import pokebase as pb
import requests, json
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from pprint import pprint
from PIL import Image
from io import BytesIO

# creating flask appliation
app = Flask(__name__)

# passing app to bootstrap
bootstrap = Bootstrap5(app)

# Homepage
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

# Worked on by: Pedro
# Pokemon info route
@app.route('/info/<transformation>/<name>')
def info(transformation, name):
    pokemon = pb.pokemon(name)
    bio = pokemon.species.flavor_text_entries[0].__dict__['flavor_text']
    img_url = "https://cdn.traction.one/pokedex/pokemon/" + str(pokemon.id) + ".png"

    response = requests.get(img_url)

    img = Image.open(BytesIO(response.content))
    img_tag = transform_image(img, transformation)

    stats = preprocess_stats(pokemon.stats)

    # try except to preprocess pokemon's evolution data
    try:
        r = requests.get(pokemon.species.evolution_chain.url)
        data = r.json()
        evolution_dict = preprocess_evolution(data["chain"])
    except:
        print('error')

    # preprocess generation data
    gen_dict = preprocess_versions(pokemon.sprites.versions.__dict__, pokemon.id)
    habitats = {}
    
    for i in range(1, 10):
        habitat = pb.pokemon_habitat(i)
        habitats[habitat.name] = habitat.pokemon_species
    
    habitat_list = preprocess_habitats(habitats, pokemon.name)

    print(habitat_list)
    
    return render_template('info.html', pokemon=pokemon, img_tag=img_tag, bio=bio, stats=stats, evolution_dict=evolution_dict, gen_dict=gen_dict, habitat_list=habitat_list)
  
# Lists Pokemon types
@app.route('/types')
def types():
    return render_template('types.html')
