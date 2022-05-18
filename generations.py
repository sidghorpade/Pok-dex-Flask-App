# generations.py
# Worked on by: Pedro
# Description: Holds functions and data used by the generations route in main.py

from main import *

# Returns preprocessed dictionary of every Pokemon by generation
def preprocess_gen_pokemon(generations):
    gen_pokemon = {}
    for generation in generations:
        pokemon_list = []
        for pokemon in generation.pokemon_species:
            pokemon_dict = {}
            pokemon_dict['id'] = int(pokemon.url.split('/')[-2])
            pokemon_dict['name'] = pokemon.name
            pokemon_list.append(pokemon_dict)
            

        pokemon_list = sorted(pokemon_list, key=lambda d: d['id'])
        gen_pokemon[generation.name.split('-')[-1]] = pokemon_list

    return gen_pokemon

# Mapping generation roman numerals to regular numbers for route purposes
gen_number_dict = {
    'i': 1,
    'ii': 2,
    'iii': 3,
    'iv': 4, 
    'v': 5,
    'vi': 6,
    'vii': 7,
    'viii': 8
}

game_dict = {
        'i': ['red', 'blue', 'yellow'],
        'ii': ['gold', 'silver', 'crystal'],
        'iii': ['ruby', 'sapphire', 'emerald', 'firered', 'leafgreen'],
        'iv': ['diamond', 'pearl', 'platinum', 'heartgold', 'soulsilver'],
        'v': ['black', 'white', 'black2', 'white2'],
        'vi': ['x', 'y', 'omegaruby', 'alphasapphire'],
        'vii': ['sun', 'moon', 'ultrasun', 'ultramoon'],
        'viii': ['sword', 'shield', 'brilliantdiamond', 'shiningpearl']
    }