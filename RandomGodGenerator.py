# This is the functions and helpers that runs the generate_god program
import FantasyGod
import json
import random

with open(r"random_generator.json") as data_file:
    RANDOM_GENERATOR = json.load(data_file)


def pick_god_gender(sphere: str) -> str:
    """
    Decides what gender the god will have based on the sphere of the god using the random.choice method and lists.
    """
    if sphere == "good":
        return random.choice(["male"] * 6 + ["female"] * 6 + ["nonb"] * 2)
    if sphere == "neutral":
        return random.choice(["male"] * 6 + ["female"] * 6 + ["nonb"] * 2)
    if sphere == "evil":
        return random.choice(["male"] * 6 + ["female"] * 6 + ["nonb"] * 2)
    if sphere == "eldritch":
        return random.choice(["male"] * 3 + ["female"] * 2 + ["uncomp"] * 7 + ["force"] * 3)
    if sphere == "force":
        return "force"
    else:
        return "error"


def pick_god_name(sphere: str, gender: str) -> str:
    """
    Basically uses the sphere and gender of the god and assign it a name using the random.choice method and lists.
    """
    if sphere == "good" and gender == "male":
        return random.choice(RANDOM_GENERATOR["good male name"])
    if sphere == "good" and gender == "female":
        return random.choice(RANDOM_GENERATOR["good female name"])
    if sphere == "good" and gender == "nonb":
        return random.choice(RANDOM_GENERATOR["good nonb name"])
    if sphere == "neutral" and gender == "male":
        return random.choice(RANDOM_GENERATOR["neutral male name"])
    if sphere == "neutral" and gender == "female":
        return random.choice(RANDOM_GENERATOR["neutral female name"])
    if sphere == "neutral" and gender == "nonb":
        return random.choice(RANDOM_GENERATOR["neutral nonb name"])
    if sphere == "evil" and gender == "male":
        return random.choice(RANDOM_GENERATOR["evil male name"])
    if sphere == "evil" and gender == "female":
        return random.choice(RANDOM_GENERATOR["evil female name"])
    if sphere == "evil" and gender == "nonb":
        return random.choice(RANDOM_GENERATOR["evil nonb name"])
    if sphere == "force" and gender == "force":
        return random.choice(RANDOM_GENERATOR["force part 1 name"]) + " of " + random.choice(
            RANDOM_GENERATOR["force part 2 name"])
    if sphere == "eldritch":
        return random.choice(RANDOM_GENERATOR["eldritch name"])
    else:
        return "error"


def pick_god_of1(sphere: str, name: str) -> str:
    """
    Chooses what sphere the god is going to be based on the name and the god"s sphere, with some name"s getting the odds modified
    to give them a more likely chance of getting an attribute that defines them. Uses random.choice method and lists.
    """
    of_list = ["air", "earth", "fire", "water", "time", "storms", "metals", "unseen forces", "fertility", "stars",
               "oceans", "volcanos", "seasons", "afterlife"]
    if sphere == "good":
        of_list.extend(RANDOM_GENERATOR["good god of 1"])
    if sphere == "neutral":
        of_list.extend(RANDOM_GENERATOR["neutral god of 1"])
    if sphere == "evil":
        of_list.extend(RANDOM_GENERATOR["evil god of 1"])
    if sphere == "force":
        of_list.extend(RANDOM_GENERATOR["force god of 1"])
    if sphere == "eldritch":
        of_list.extend(RANDOM_GENERATOR["eldritch god of 1"])
    # sphere above, name below; add more later, may never happen
    if "Devil" in name:
        of_list.extend(["chaos", "chaos", "chaos", "murder", "murder", "murder"])
    if "Edin" in name:
        of_list.extend(["life", "life", "life", "nature", "nature", "nature"])
    return random.choice(of_list)


def pick_god_of2(sphere: str, name: str, god_of: str) -> str:
    """
    Chooses what sphere the god is going to be based on the name and the god"s sphere, with some name"s getting the odds modified
    to give them a more likely chance of getting an attribute that defines them. Uses random.choice method and lists. This list is more
    about the personality of the god. All will merge with json file
    """
    of_list = []
    if sphere == "good":
        of_list.extend(RANDOM_GENERATOR["good god of 2"])
    if sphere == "neutral":
        of_list.extend(RANDOM_GENERATOR["neutral god of 2"])
    if sphere == "evil":
        of_list.extend(RANDOM_GENERATOR["evil god of 2"])
    if sphere == "force":
        of_list.extend(RANDOM_GENERATOR["force god of 2"])
    if sphere == "eldritch":
        of_list.extend(RANDOM_GENERATOR["eldritch god of 2"])

    if not of_list:
        return "error"
    return random.choice(of_list)


def pick_god_involvement(sphere: str, fantasy_level: int) -> int:
    """
    Using sphere and fantasy level, an equation using some rng from random.choice, is performed.
    An involvement level between 4 and 5 is a moderate level of involvement from a god. Something like
    2 or a 3 would mean the god is disinterested and anything higher than a 7 means the god is really
    a busybody.
    """
    if sphere == "good" or sphere == "evil":
        involvement = random.choice([1, 2, 3, 4, 5]) + fantasy_level
    elif sphere == "neutral":
        involvement = random.choice([1, 2, 3, 4, 5]) + fantasy_level - 1
    elif sphere == "eldritch":
        involvement = fantasy_level - random.choice([2, 3, 4, 5])
        if involvement < 0:
            involvement = 0
    elif sphere == "force":
        involvement = fantasy_level + 1
    return involvement


def pick_god_angel_like(sphere: str, involvement_level: int, fantasy_level: int) -> bool:
    """
    Using different formulas for each sphere (good and evil use the same), a random
    function is used to determined whether a god has angels or not. Involvement Level and
    Fantasy Level come into play. FORMULA NOT FINAL!
    """
    if sphere == "good" or sphere == "evil":
        if involvement_level > 8:
            number = -1
        elif 5 < involvement_level < 8:
            number = 2
        else:
            number = 0
        al_list = [True] * (fantasy_level + number + 1) + [False] * (fantasy_level + 1)
    elif sphere == "neutral":
        if involvement_level > 7:
            number = 2
            number2 = 0
        elif involvement_level < 3:
            number = 0
            number2 = 3
        else:
            number = 0
            number2 = 2
        al_list = [True] * (fantasy_level + number + 1) + [False] * (fantasy_level + number2 + 1)
    elif sphere == "eldritch":
        if involvement_level > 7:
            number = 3
        else:
            number = 0
        al_list = [True] * (fantasy_level + number + 1) + [False] * 8
    elif sphere == "force":
        al_list = [True] * 1 + [False] * 7
    return random.choice(al_list)


def pick_god_incarnate(sphere: str, involvement_level: int, fantasy_level: int) -> bool:
    """
    Using different formulas for each sphere (good and evil use the same), a random
    function is used to determined whether a god has angels or not. Involvement Level and
    Fantasy Level come into play. FORMULA NOT FINAL!
    """
    if sphere == "good" or sphere == "evil":
        if involvement_level > 8:
            number = 2
        elif 5 < involvement_level < 8:
            number = 0
        else:
            number = 1
        gi_list = [True] * (fantasy_level + number) + [False] * fantasy_level
    elif sphere == "neutral":
        if involvement_level > 7:
            number = 2
            number2 = 1
        elif involvement_level < 3:
            number = 1
            number2 = 2
        else:
            number = 2
            number2 = 1
        gi_list = [True] * (fantasy_level + number) + [False] * (fantasy_level + number2)
    elif sphere == "eldritch":
        if involvement_level > 8:
            number = 3
        else:
            number = 1
        value = (fantasy_level + number)
        if value < 1:
            gi_list = [False]
        else:
            gi_list = [True] * value + [False] * 8
    elif sphere == "force":
        gi_list = [False]
    return random.choice(gi_list)


def genBeastFant(base) -> str:
    if base == "beast":
        base = random.choice(RANDOM_GENERATOR["beast templates"])
    elif base == "half-beast":
        base = random.choice(RANDOM_GENERATOR["half-beast templates"])
    elif base == "fantacreature":
        base = random.choice(RANDOM_GENERATOR["fantacreature templates"])
    return base


def generate_app_base(sph) -> str:
    """
    Gets the template appearance for a god that will later influence
    their traits. Will also add more descriptors later.
    """
    base = ""
    if sph == "good":
        base = random.choice(RANDOM_GENERATOR["good god base templates"])
    elif sph == "neutral":
        base = random.choice(RANDOM_GENERATOR["neutral god base templates"])
    elif sph == "evil":
        base = random.choice(RANDOM_GENERATOR["evil god base templates"])
    elif sph == "force":
        base = random.choice(RANDOM_GENERATOR["force god base templates"])
    elif sph == "eldritch":
        base = random.choice(RANDOM_GENERATOR["eldritch god base templates"])

    # custom stuff beasts, half-beasts, and fantasy creatures.
    base = genBeastFant(base)
    return base


def generate_form_trait(sph, gen, g_of1, g_of2, base, trait_exceptions_list) -> str:
    trait = ""
    trait_rand_list = []

    # types-of
    if base == "humanoid":
        trait_rand_list.extend(RANDOM_GENERATOR["human forms"])
    elif base in RANDOM_GENERATOR["beast templates"] or base in RANDOM_GENERATOR["fantacreature templates"] or base in \
            RANDOM_GENERATOR["half-beast templates"]:
        trait_rand_list.extend(RANDOM_GENERATOR["beast/hb forms"])
    elif base == "angel-like":
        trait_rand_list.extend(RANDOM_GENERATOR["angel forms"])
    elif base == "demon-like":
        trait_rand_list.extend(RANDOM_GENERATOR["demon forms"])
    elif base == "visible force":
        trait_rand_list.extend(RANDOM_GENERATOR["vis force forms"])
    elif base == "invisible force":
        trait_rand_list.extend(RANDOM_GENERATOR["invis force forms"])
    elif "tentacled behemoth" == base:
        trait_rand_list.extend(RANDOM_GENERATOR["tentacle forms"])
    elif "contorted humanoid" == base:
        trait_rand_list.extend(RANDOM_GENERATOR["cont forms"])
    elif "winged horror" == base:
        trait_rand_list.extend(RANDOM_GENERATOR["winged forms"])
    # get trait
    trait = random.choice(trait_rand_list)
    return trait


def generate_phys_trait(sph, gen, g_of1, g_of2, base, trait_exceptions_list) -> str:
    trait = ""
    trait_rand_list = []

    # types-of
    if base == "humanoid":
        trait_rand_list.extend(RANDOM_GENERATOR["human phys"])
    elif base in RANDOM_GENERATOR["beast templates"] or base in RANDOM_GENERATOR["fantacreature templates"] or base in \
            RANDOM_GENERATOR["half-beast templates"]:
        trait_rand_list.extend(RANDOM_GENERATOR["beast/hb phys"])
    elif base == "angel-like":
        trait_rand_list.extend(RANDOM_GENERATOR["angel phys"])
    elif base == "demon-like":
        trait_rand_list.extend(RANDOM_GENERATOR["demon phys"])
    elif base == "visible force":
        trait_rand_list.extend(RANDOM_GENERATOR["vis force phys"])
    elif base == "invisible force":
        trait_rand_list.extend(RANDOM_GENERATOR["invis force phys"])
    elif "tentacled behemoth" == base:
        trait_rand_list.extend(RANDOM_GENERATOR["tentacle phys"])
    elif "contorted humanoid" == base:
        trait_rand_list.extend(RANDOM_GENERATOR["cont phys"])
    elif "winged horror" == base:
        trait_rand_list.extend(RANDOM_GENERATOR["winged phys"])
    # get trait
    trait = random.choice(trait_rand_list)
    return trait


def generate_item_trait(sph, gen, g_of1, g_of2, base, trait_exceptions_list) -> str:
    trait = ""
    trait_rand_list = []
    if base == "humanoid" or base == "angel-like" or base == "demon-like":
        trait_rand_list = RANDOM_GENERATOR["human-adj items"]
    else:
        trait_rand_list = RANDOM_GENERATOR["non-adj items"]
    trait = random.choice(trait_rand_list)
    return trait


def generate_app_countenance(sph, g_of1, g_of2, base) -> str:
    count = ""
    if sph == "good":
        count = random.choice(RANDOM_GENERATOR["good god countenance"])
    elif sph == "neutral":
        count = random.choice(RANDOM_GENERATOR["neutral god countenance"])
    elif sph == "evil":
        count = random.choice(RANDOM_GENERATOR["evil god countenance"])
    elif sph == "force":
        count = random.choice(RANDOM_GENERATOR["force god countenance"])
    elif sph == "eldritch":
        count = random.choice(RANDOM_GENERATOR["eldritch god countenance"])
    return count


def generate_god_appearance(sph, gen, g_of1, g_of2) -> dict:
    base = generate_app_base(sph)
    trait1 = generate_form_trait(sph, gen, g_of1, g_of2, base, [])
    trait2 = generate_phys_trait(sph, gen, g_of1, g_of2, base, [trait1])
    trait3 = generate_item_trait(sph, gen, g_of1, g_of2, base, [trait1, trait2])
    countenance = generate_app_countenance(sph, g_of1, g_of2, base)
    return {"base": base, "form": trait1, "phys": trait2, "item": trait3, "countenance": countenance}


# below are god generators we can use to tool our program


def generateTotallyRandomGodNonPan(fant_lvl: int) -> FantasyGod:
    sph = random.choice(["good", "neutral", "evil", "force", "eldritch"])
    gen = pick_god_gender(sph)
    nm = pick_god_name(sph, gen)
    g_of1 = pick_god_of1(sph, nm)
    g_of2 = pick_god_of2(sph, nm, g_of1)
    inv = pick_god_involvement(sph, fant_lvl)
    ang = pick_god_angel_like(sph, inv, fant_lvl)
    inc = pick_god_incarnate(sph, inv, fant_lvl)
    pan = False
    appearance = generate_god_appearance(sph, gen, g_of1, g_of2)
    god = FantasyGod.FantasyGod(nm, sph, gen, g_of1, g_of2, inv, ang, pan, inc, appearance)
    return god


def generateGenderedGodNonPan(fant_lvl: int, gender: str) -> FantasyGod:
    sph = random.choice(["good", "neutral", "evil", "force", "eldritch"])
    gen = gender
    nm = pick_god_name(sph, gen)
    g_of1 = pick_god_of1(sph, nm)
    g_of2 = pick_god_of2(sph, nm, g_of1)
    inv = pick_god_involvement(sph, fant_lvl)
    ang = pick_god_angel_like(sph, inv, fant_lvl)
    inc = pick_god_incarnate(sph, inv, fant_lvl)
    pan = False
    appearance = generate_god_appearance(sph, gen, g_of1, g_of2)
    god = FantasyGod.FantasyGod(nm, sph, gen, g_of1, g_of2, inv, ang, pan, inc, appearance)
    return god


def generateSpheredGodNonPan(fant_lvl: int, sphere: str) -> FantasyGod:
    sph = sphere
    gen = pick_god_gender(sph)
    nm = pick_god_name(sph, gen)
    g_of1 = pick_god_of1(sph, nm)
    g_of2 = pick_god_of2(sph, nm, g_of1)
    inv = pick_god_involvement(sph, fant_lvl)
    ang = pick_god_angel_like(sph, inv, fant_lvl)
    inc = pick_god_incarnate(sph, inv, fant_lvl)
    pan = False
    appearance = generate_god_appearance(sph, gen, g_of1, g_of2)
    god = FantasyGod.FantasyGod(nm, sph, gen, g_of1, g_of2, inv, ang, pan, inc, appearance)
    return god


def generateTooledGodNonPan(fant_lvl: int, sphere: str, gender: str, g_of1: str) -> FantasyGod:
    sph = sphere
    gen = gender
    nm = pick_god_name(sph, gen)
    g_of1 = g_of1
    g_of2 = pick_god_of2(sph, nm, g_of1)
    inv = pick_god_involvement(sph, fant_lvl)
    ang = pick_god_angel_like(sph, inv, fant_lvl)
    inc = pick_god_incarnate(sph, inv, fant_lvl)
    pan = False
    appearance = generate_god_appearance(sph, gen, g_of1, g_of2)
    god = FantasyGod.FantasyGod(nm, sph, gen, g_of1, g_of2, inv, ang, pan, inc, appearance)
    return god


def generatePanGod(fant_lvl: int, pan_member: FantasyGod):
    if pan_member.sphere == 'good' or pan_member.sphere == 'neutral' or pan_member.sphere == 'evil':
        sph = random.choice(["good", "neutral", "evil"])
    else:
        sph = pan_member.sphere
    gen = pick_god_gender(sph)
    nm = pick_god_name(sph, gen)
    g_of1 = pick_god_of1(sph, nm)
    g_of2 = pick_god_of2(sph, nm, g_of1)
    inv = pick_god_involvement(sph, fant_lvl)
    ang = pick_god_angel_like(sph, inv, fant_lvl)
    inc = pick_god_incarnate(sph, inv, fant_lvl)
    pan = True
    appearance = generate_god_appearance(sph, gen, g_of1, g_of2)
    god = FantasyGod.FantasyGod(nm, sph, gen, g_of1, g_of2, inv, ang, pan, inc, appearance)
    return god


# playground below where I mess around with my generators


Adam = generateTotallyRandomGodNonPan(3)
print("\n")
Adam.printGod()
