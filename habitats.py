# habitats.py
# Description: Holds functions and data used by the habitats route in main.py

# Returns preprocessed dictionary of habitats
# Key: Habitat Name
# Value: Dictionary
#        Keys: Pokemon list, Habitat description

import pokebase as pb

def habitats_dict():
    habitats = {}

    for i in range (1, 10):
        habitat = pb.pokemon_habitat(i)
        dict = {
            'pokemon': habitat.pokemon_species,
            'description': habitat_descriptions[habitat.name]
        }
        habitats[habitat.name] = dict

    return habitats

# Dictionary of descriptions for each habitat
habitat_descriptions = {
    'cave': 'Little to no light penetrates into dark, damp caverns. Mineral-rich Ground-, Rock-, and Steel-types can often be found underground alongside a variety of Pokémon adapted to life in the dark. Some Dragon-types also have a preference to hide themselves deep within winding caves.',
    'forest': 'Most trainers are familiar with temperate, broadleaf forests. With mild, but seasonal weather and healthy tree growth, they play home to many common Pokémon. Many types can be found in these forests, but Grass-, Bug-, Flying-, and Normal-types are the most abundant. Novice trainers would do well starting their adventures in such areas.',
    'grassland': 'Characterized by a lack of tall trees and an abundance of tall grass. They are warm with seasonal rainfall; dry seasons are exceptionally devoid of water. Brushfires are an occasional occurrence in these areas, a phenomenon exacerbated by Fire- and Electric-types that can start them. Poison- and Normal-types are also a regular sight in the tall grass.',
    'mountain': 'This biome specifically refers to the open-faced, rugged mountainsides ideal for Rock- and Steel-types; mountain forests and peaks usually support a different set of Pokémon entirely. These places are also remote and usually quiet, so Fighting-types often find refuge on them so they can train in peace.',
    'rare': 'Rare, legendary Pokemon can be found in a variety of habitats. Since many of these Pokemon are one of a kind it is impossible to clasify a sole category for where they can be found. Some rare Pokemon include Mewtwo, Celebi, Arceus, Lugia, and many more!',
    'rough-terrain': 'Sandy, arid deserts support many Ground-type Pokémon that can burrow away from the sun\'s heat. Many other hardy species of Pokémon, however, have also adapted to a life of sweltering days and frigid nights. Desert dwellers also usually require very little water for survival or have some way of storing it for long periods of time.',
    'sea': 'Warm, sunlit waters and vibrant coral reefs provide the Water-types that dwell here with abundant food and shelter, making them the richest ecosystems in the world. Marine Pokémon of all kinds can be found in these tropical havens, which are particularly sensitive to changes in water temperature, salinity, and cleanliness.',
    'urban': 'Urban areas like cities are defined by the humans that live in them and the environments that they create. Some Pokémon only can live parts of their lives in cities, while others happily inhabit walkways, alleys, or even homes as pets--or pests. Normal-, Psychic-, Fighting-, and Ghost-type Pokémon often coexist alongside people, while Poison-types even thrive on the waste that we create.',
    'waters-edge': 'Rocky and sandy beaches play home to many semiaquatic Pokémon that are content only spending some of their time in the sea. The intertidal zone also supports rock pools where some hardier Water-types make their homes; Pokémon that dwell here are adapted to withstand crashing waves and changing tides.'
}