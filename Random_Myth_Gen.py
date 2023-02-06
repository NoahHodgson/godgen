import God
import Fantasy_World
import json
import random

import Random_God_Generator as Random_God_Generator

with open(r"JSON/random_generator_myth_parts.json") as data_file:
    RANDOM_GENERATOR = json.load(data_file)  # note, loading from loading from a different file than


def creation_event_generator(new_world, sphere):
    pre_uni = random.choice(RANDOM_GENERATOR["Pre-Universe"])
    creation_event = "In the beginning there was " + pre_uni + ". Then "
    if sphere == "good":
        creation_event += random.choice(RANDOM_GENERATOR["Good Creation Event"])
    elif sphere == "neutral":
        creation_event += random.choice(RANDOM_GENERATOR["Neutral Creation Event"])
    elif sphere == "evil":
        creation_event += random.choice(RANDOM_GENERATOR["Evil Creation Event"])
    else:
        return "ERROR"

    if "CREATOR" in creation_event:
        god = Random_God_Generator.generate_sphered_god_non_pan(new_world.fantasy_level, sphere)
        new_world.live_gods["creator"] = god
        new_world.all_gods["creator"] = god
        creation_event = creation_event.replace("CREATOR", god.name)
        creation_event = creation_event.replace("CREATOR"+"'s", god.name+"'s")

    if "DEAD_GOOD_GOD" in creation_event:
        god = Random_God_Generator.generate_sphered_god_non_pan(new_world.fantasy_level, "good")
        new_world.live_gods[god.name] = god
        new_world.all_gods[god.name] = god
        creation_event = creation_event.replace("DEAD_GOOD_GOD", god.name)
    
    if "DEAD_NEUTRAL_GOD" in creation_event:
        god = Random_God_Generator.generate_sphered_god_non_pan(new_world.fantasy_level, "neutral")
        new_world.live_gods[god.name] = god
        new_world.all_gods[god.name] = god
        creation_event = creation_event.replace("DEAD_NEUTRAL_GOD", god.name)
    
    if "DEAD_EVIL_GOD" in creation_event:
        god = Random_God_Generator.generate_sphered_god_non_pan(new_world.fantasy_level, "evil")
        new_world.live_gods[god.name] = god
        new_world.all_gods[god.name] = god
        creation_event = creation_event.replace("DEAD_EVIL_GOD", god.name)

    if "GOOD_GOD" in creation_event:
        god = Random_God_Generator.generate_sphered_god_non_pan(new_world.fantasy_level, "good")
        new_world.live_gods[god.name] = god
        new_world.all_gods[god.name] = god
        creation_event = creation_event.replace("GOOD_sGOD", god.name)

    if "NEUTRAL_GOD" in creation_event:
        god = Random_God_Generator.generate_sphered_god_non_pan(new_world.fantasy_level, "neutral")
        new_world.live_gods[god.name] = god
        new_world.all_gods[god.name] = god
        creation_event = creation_event.replace("NEUTRAL_GOD", god.name)
    
    if "EVIL_GOD" in creation_event:
        god = Random_God_Generator.generate_sphered_god_non_pan(new_world.fantasy_level, "evil")
        new_world.live_gods[god.name] = god
        new_world.all_gods[god.name] = god
        creation_event = creation_event.replace("EVIL_GOD", god.name)
    
    if "PLANET" in creation_event:
        creation_event = creation_event.replace("PLANET", new_world.name)

    creation_event += " Thus began the " + random.choice(["realm ","planet ","Plane of "]) + new_world.name + "."
    new_world.events.append(creation_event)
    return creation_event

# Break into wayyy more functions
def early_event_generator(world):
    return


def generate_random_young_world(fant_lvl) -> Fantasy_World:
    mwa = 15 # this is going to change, get way bigger
    ge_lvl = 5  # out of 10, make separate function so we can have many different ones.
    world_name = random.choice(RANDOM_GENERATOR["World Name"])
    new_world = Fantasy_World.Fantasy_World(world_name, ge_lvl, mwa, fant_lvl)
    pantheon = random.choice([True, False])
    creator_alignment = random.choice(["good", "neutral", "evil"])
    creation_event_generator(new_world, creator_alignment)
    if len(new_world.live_gods) > 0:
        list(new_world.live_gods.values())[0].print_god()
        print("\n")
    # updating good and evil level make this a function
    if list(new_world.live_gods.values())[0].sphere == 'good':
        ge_lvl += 1
    elif list(new_world.live_gods.values())[0].sphere or new_world.live_gods[0].sphere == 'force':
        pass
    else:
        ge_lvl -= 1
    return new_world

# playground below where I mess around with my generators
print("\n")
print(generate_random_young_world(3).events[0])
print("\n")

