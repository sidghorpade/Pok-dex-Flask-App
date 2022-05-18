# Title: main.py
# Description: Holds Flask application code and all routes to web pages

import os
from ensurepip import version
from info import preprocess_bio, preprocess_evolution, preprocess_versions, preprocess_stats, preprocess_habitats
from transformations import transform_image
from generations import gen_number_dict, preprocess_gen_pokemon
import random
import pokebase as pb
import requests, json
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
from flask import Flask, render_template, request, redirect,url_for, abort, send_from_directory
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap5
from pprint import pprint
from PIL import Image
from io import BytesIO
from poke_info import *
import imghdr

# creating flask appliation
app = Flask(__name__)
app.config['SECRET_KEY'] = 'pokemain'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'uploads'

# passing app to bootstrap
bootstrap = Bootstrap5(app)

class Pokemon(FlaskForm):
    pokemon_name = StringField('Pokemon', validators=[DataRequired()] )   

#Pass search
@app.context_processor
def base():
    form = Pokemon()
    return dict(form=form)

# Homepage
@app.route('/', methods=('GET', 'POST'))
def home():
    form = Pokemon()
    if form.validate_on_submit():
        info.pokemon =form.pokemon_name.data
        return redirect('/info',form=form, pokemon_name = info.pokemonn)
    return render_template('home.html')

# Worked on by: Pedro
# Generations route
@app.route('/generations')
@app.route('/generations/<id>')
def generations(id=None):
    generations = []

    if id != None:
        id = gen_number_dict[id]

    gen_pokemon = {}
    for gen in range(1, 9):
        generations.append(pb.generation(gen))
    
    gen_pokemon = preprocess_gen_pokemon(generations)

    games = {
        'i': ['red', 'blue', 'yellow'],
        'ii': ['gold', 'silver', 'crystal'],
        'iii': ['ruby', 'sapphire', 'emerald', 'firered', 'leafgreen'],
        'iv': ['diamond', 'pearl', 'platinum', 'heartgold', 'soulsilver'],
        'v': ['black', 'white', 'black2', 'white2'],
        'vi': ['x', 'y', 'omegaruby', 'alphasapphire'],
        'vii': ['sun', 'moon', 'ultrasun', 'ultramoon'],
        'viii': ['sword', 'shield', 'brilliantdiamond', 'shiningpearl']
    }
        
    return render_template('generations.html', id=id, generations=generations, gen_pokemon=gen_pokemon, games=games)

# Worked on by: Pedro
# Pokemon info route
@app.route('/info/<transformation>/<name>')
def info(transformation, name):
    pokemon = pb.pokemon(name)
    bio = preprocess_bio(pokemon.species.flavor_text_entries)

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
    no_habitats = len(habitat_list) == 0

    print(len(habitat_list))
    
    return render_template('info.html', pokemon=pokemon, img_tag=img_tag, bio=bio, stats=stats, evolution_dict=evolution_dict, gen_dict=gen_dict, habitat_list=habitat_list, no_habitats=no_habitats)
  
# Lists Pokemon types
@app.route('/types')
def types():
    return render_template('types.html')

# Pokemon Type Pages
@app.route('/types/<type>')
def selectedType(type):
    poke_list = []

    i = 0
    while i < len(poke_info):
        temp_dict = {}

        for key in poke_info[i]:
            if poke_info[i]['type'] == type:
                temp_dict.update({key:poke_info[i][key]})

        if len(temp_dict) > 0:
            poke_list.append(temp_dict)

        i +=1
    
    limit = len(poke_list)
    return render_template('selectedType.html', poke_list = poke_list, type = type, limit = limit)

# Search by image route
@app.route('/searchByImage')
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('searchByImage.html', files=files)

