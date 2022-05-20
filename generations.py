# generations.py
# Worked on by: Pedro
# Description: Holds functions and data used by the generations route in main.py

from main import *

# Returns preprocessed dictionary of every Pokemon by generation
def preprocess_gen_pokemon(generations):
    gen_pokemon = {}

    # Loop through each generatin
    for generation in generations:
        pokemon_list = []
        # Loop through each Pokemon in current generation
        for pokemon in generation.pokemon_species:
            pokemon_dict = {}
            # Will store metadata for each pokemon in a list for current generation
            pokemon_dict['id'] = int(pokemon.url.split('/')[-2])
            pokemon_dict['name'] = pokemon.name
            pokemon_list.append(pokemon_dict)
            
        # Sort the Pokemon list by their ID
        pokemon_list = sorted(pokemon_list, key=lambda d: d['id'])
        # Add list to our dictionary
        # Key is roman numeral representation of the generation number
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

# Mapping generation roman numerals to list of games associated with each generation
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

# Mapping generation name to description metadata (release year and short description of the generation's region)
# Descriptions from: https://bulbapedia.bulbagarden.net/wiki/
gen_descriptions = {
    'generation-i': {
        'year': 1996,
        'description': 'The Kanto region (Japanese: カントー地方 Kanto region) is a region of the Pokémon world. Kanto is located east of Johto, which together form a joint landmass that is south of Sinnoh.'
    },
    'generation-ii': {
        'year': 1999,
        'description': 'The Johto region (Japanese: ジョウト地方 Johto region) is a region of the Pokémon world. Johto is located west of Kanto, which together form a joint landmass that is south of Sinnoh and Sinjoh Ruins.'
    },
    'generation-iii': {
        'year': 2002,
        'description': 'The Hoenn region (Japanese: ホウエン地方 Hoenn region) is a region of the Pokémon world. It is located south of Sinnoh, as stated in The Unbeatable Lightness of Seeing!. It is the setting of Pokémon Ruby, Sapphire, Emerald, Omega Ruby, and Alpha Sapphire. It was the third core series region to be introduced.'
    },
    'generation-iv': {
        'year': 2006,
        'description': 'The Sinnoh region (Japanese: シンオウ地方 Sinnoh region), formerly known as Hisui (Japanese: ヒスイ地方 Hisui region), is a region of the Pokémon world. It is located north of Kanto,[1] Johto,[1] and Hoenn.[2] It is the setting of Pokémon Diamond, Pearl, Platinum, Brilliant Diamond, Shining Pearl, and Legends: Arceus; the latter explores the region\'s earlier history when it was still known as Hisui. It was the fourth core series region to be introduced.'
    }, 
    'generation-v': {
        'year': 2010,
        'description': 'The Unova region (Japanese: イッシュ地方 Isshu region) is a region of the Pokémon world. It is the setting of Pokémon Black and White and Pokémon Black 2 and White 2. It was the fifth core series region to be introduced. Unova is far away from the four other large regions, and the Pokémon which inhabit Unova are diverse and different from those of Kanto, Johto, Hoenn, and Sinnoh.'
    },
    'generation-vi': {
        'year': 2013,
        'description': 'The Kalos region (Japanese: カロス地方 Kalos region) is a region of the Pokémon world. It was the sixth core series region to be introduced and is the setting of Pokémon X and Y. It is shaped like a five-pointed star, with one of its biggest cities being Lumiose City in the north-central part of the region.'
    },
    'generation-vii': {
        'year': 2016,
        'description': 'The Alola region (Japanese: アローラ地方 Alola region) is a region of the Pokémon world. It was the seventh core series region to be introduced and is the setting of Pokémon Sun, Moon, Ultra Sun, and Ultra Moon. Alola is made up of five islands: the natural islands Melemele Island, Akala Island, Ula\'ula Island, and Poni Island; and the artificial island Aether Paradise.'
    },
    'generation-viii': {
        'year': 2019,
        'description': 'The Galar region (Japanese: ガラル地方 Galar region) is a region of the Pokémon world, and the eighth core series region to be introduced. It is the setting of Pokémon Sword and Shield. The layout of the region is the most vertical by far.'
    }
}