# Title: info.py
# Worked on by: Pedro
# Description: Holds functions and/or data used by the info route in main.py

from main import *

# Returns preprocessed dictionary of a pokemon's evolution chain
# Key: Pokemon ID
# Value: Name
def preprocess_evolution(evolution_json):
    evolution_dict = {}
    
    # While loop will run until end of evolution chain is reached
    while True:
        name = evolution_json["species"]["name"]
        id = evolution_json["species"]["url"].split('/')[-2]

        evolution_dict[id] = name

        # If this length is not 0, end of chain has not been reached
        if len(evolution_json["evolves_to"]) != 0:
            evolution_json = evolution_json["evolves_to"][0]
        else:
            break

    return evolution_dict

# Returns preprocessed dictionary of the generations and games that a pokemon appears in
# Key: Gen Numbers
# Values: Pokemon Sprite
#         Array of Games
def preprocess_versions(generations, id):
    gen_dict = {}
    gens_to_delete = []

    # Determines which generations a pokemon is not a part of
    for generation in generations:
        if generation_counts[generation] < id:
            gens_to_delete.append(generation)
        else:
            break

    # Deletes irrelevant generation data
    for gen in gens_to_delete:
        del generations[gen]

    # Parse through remaining generations to generation 
    # a preprocessed generation dictionary
    for generation in generations:
        games = generations[generation].__dict__
        # This will be index for new dictionary
        gen_num = generation.split('-')[-1]

        game_names = []
        sprite = ""

        # Parse through games in current generation to
        # see which games this pokemon appears in
        for game in games:
            front_sprite = games[game].__dict__["front_default"]
            # If there is a front sprite, the pokemon appears in current game
            if front_sprite != None:
                sprite = front_sprite
                names = game.split('-')
                # Does some checks because of weird API data to ensure correct values are stored in dictionary
                for name in names:
                    if name == 'icons':
                        if generation == 'generation-vii':
                            game_names.append('sun')
                            game_names.append('moon')
                        elif generation == 'generation-viii':
                            game_names.append('sword')
                            game_names.append('shield')
                    elif name == 'ultra':
                        game_names.append('ultrasun')
                        game_names.append('ultramoon')
                        break
                    else:
                        game_names.append(name)

        # Include Black & White 2
        if generation == 'generation-v':
            game_names.append('black2')
            game_names.append('white2')

        # Append new entry into our the dictionary
        data = {}
        data["sprite"] = sprite
        data["games"] = game_names
        gen_dict[gen_num] = data
    
    return gen_dict

# Returns preprocessed dictionary of a Pokemon's stats
# Key: Stat Name
# Value: Stat Value
def preprocess_stats(stats):
    stats_dict = {}

    for stat in stats:
        base_stat = stat.__dict__['base_stat']
        name = stat.__dict__['stat'].__dict__['name']
        stats_dict[name] = base_stat

    print(stats_dict)
    return stats_dict

# Returns prepocessed list of habitats a Pokemon is found in
def preprocess_habitats(habitats, name):
    habitat_list = []

    for habitat in habitats:
        pokemon = habitats[habitat]
        for p in pokemon:
            if p.name == name:
                habitat_list.append(habitat)
                break

    return habitat_list

# Used to determine which generations to discard
# Values are last Pokemon ID from corresponding generation
generation_counts = {
    'generation-i': 151, 
    'generation-ii': 251, 
    'generation-iii': 386, 
    'generation-iv': 493, 
    'generation-v': 649,
    'generation-vi': 721, 
    'generation-vii': 809, 
    'generation-viii': 905
}