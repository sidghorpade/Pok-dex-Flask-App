from main import *

def preprocess_gen_pokemon(habitats):
    gen_pokemon = {}
    for habitat in habitats:
        pokemon_list = []
        for pokemon in habitat.pokemon_species:
            pokemon_dict = {}
            pokemon_dict['id'] = int(pokemon.url.split('/')[-2])
            pokemon_dict['name'] = pokemon.name
            pokemon_list.append(pokemon_dict)
            

        pokemon_list = sorted(pokemon_list, key=lambda d: d['id'])
        gen_pokemon[habitat.name.split('-')[-1]] = pokemon_list

    return gen_pokemon

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