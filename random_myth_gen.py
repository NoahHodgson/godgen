import FantasyGod
import FantasyWorld
import json
import random

import RandomGodGenerator

with open(r"random_generator_myth_parts.json") as data_file:
    RANDOM_GENERATOR = json.load(data_file)  # note, loading from loading from a different file than

def creation_event_generator(world):

    return


def main_event_generator(world):

    return


def generate_random_young_world(fant_lvl) -> FantasyWorld:
    mwa = 15
    ge_lvl = 5  # out of 10
    world_name = random.choice(RANDOM_GENERATOR)
    new_world = FantasyWorld.FantasyWorld(world_name, ge_lvl, mwa, fant_lvl)
    main_event_generator(new_world)

    pantheon = random.choice([True, False])
    if pantheon: # explicit, first got in the pantheon is the creator
        num_total_gods = random.choice(3, 5, 6, 7, 8) # check this out later when you have more gods potential
        i = 0
        while i < num_total_gods:
            god = RandomGodGenerator.generate_pan_god(fant_lvl, new_world.pantheon)
            new_world.pantheon.append(god)
            new_world.gods.append(god)
            i += 1
    else:
        god = RandomGodGenerator.generate_totally_random_god_non_pan(fant_lvl)
        new_world.gods.append(god)

    # updating good and evil level
    if new_world.gods[0].sphere == 'good':
        ge_lvl += 1
    elif new_world.gods[0].sphere == 'neutral' or new_world.gods[0].sphere == 'force':
        pass
    else:
        ge_lvl -= 1
    creation_event = "In the beginning there was " + random.choice(RANDOM_GENERATOR["Pre-Universe"])

    return new_world