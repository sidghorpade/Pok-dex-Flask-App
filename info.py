from main import *

# Worked on by: Pedro
# Returns preprocessed dictionary of a pokemon's evolution chain
# Key: ID
# Value: Name
def preprocess_evolution(evolution_json):
    evolution_dict = {}
    
    while True:
        name = evolution_json["species"]["name"]
        id = evolution_json["species"]["url"].split('/')[-2]

        evolution_dict[id] = name

        if len(evolution_json["evolves_to"]) != 0:
            evolution_json = evolution_json["evolves_to"][0]
        else:
            break

    return evolution_dict

# Worked on by: Pedro
# Returns preprocessed dictionary of the generations and games that a pokemon appears in
# Key: Gen Numbers
# Value: Array of Game Names
def preprocess_versions(generations, id):
    gen_dict = {}
    gens_to_delete = []

    for generation in generations:
        if generation_counts[generation] < id:
            gens_to_delete.append(generation)
        else:
            break

    for gen in gens_to_delete:
        del generations[gen]

    for generation in generations:
        games = generations[generation].__dict__
        gen_num = generation.split('-')[-1]

        game_names = []
        sprite = ""

        for game in games:
            front_sprite = games[game].__dict__["front_default"]
            if front_sprite != None:
                sprite = front_sprite
                names = game.split('-')
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

        if generation == 'generation-v':
            game_names.append('black2')
            game_names.append('white2')

        data = {}
        data["sprite"] = sprite
        data["games"] = game_names
        gen_dict[gen_num] = data
    
    return gen_dict

generation_names = {
    'generation-i': ['red', 'blue', 'yellow'], 
    'generation-ii': ['gold', 'silver', 'crystal'], 
    'generation-iii': ['ruby', 'sapphire', 'emerald', 'firered', 'leafgreen'], 
    'generation-iv': ['diamond', 'pearl', 'platinum', 'heartgold', 'soulsilver'], 
    'generation-v': ['white', 'black', 'white2', 'black2'],
    'generation-vi': ['x', 'y', 'omegaruby', 'alphasapphire'], 
    'generation-vii': ['sun', 'moon', 'ultrasun', 'ultramoon'], 
    'generation-viii': ['sword', 'shield']
}

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