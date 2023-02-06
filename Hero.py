import God

class Hero:
    name: str = None
    sphere: str = None
    gender: str = None
    society: str = None
    worships: God = None
    # below only true if they are incarnate form of a God
    incarnate: God = None
    # use later to flesh out heroes
    goal: str = ""

    allied_to: list = []
    enemy_of: list = []

    appearance = {
        "race": None,
        "phys": None,
        "item": None,
        "countenance":None
    }
    is_alive = True
    events = []

    def print_hero(self):
        to_print = "This is " +  self.name + " the "
        if self.sphere == "good":
            to_print += "Hero of " + self.society + ". "
        elif self.sphere == "neutral":
            to_print += "Legend of " + self.society + ". "
        elif self.sphere == "evil":
            to_print += "Villain of " + self.society + ". "
        elif self.sphere == "chaotic":
            to_print += "Pariah of " + self.society + ". "
        else:
            to_print += " ERROR "
        
        if self.worships != None:
            to_print += "They are an ardent worshipper of " + self.worships + ". "
        
        if self.incarnate != None:
            to_print += "They are the incarnate form of the god " + self.incarnate.name 
            to_print += ", the god of " + self.incarnate.god_of + ". "

        if self.goal != "":
            to_print += "They dream of " + self.goal + ". "

        to_print += self.name + " is a " + self.gender + ", who is " + self.appearance["race"]+". "
        to_print += "They look quite " + self.appearance["phys"]
        to_print += " and are known to be " + self.appearance["countenance"] + "."
        print(to_print)

    # constructor
    def __init__(self, nm, sphr, gndr, soc, worships, incarnate, allies, enemies, appearance_dict):
        self.name = nm
        self.sphere = sphr
        self.gender = gndr
        self.society = soc
        self.worships = worships
        self.incarnate = incarnate
        self.allied_to = allies
        self.enemy_of = enemies
        self.appearance = appearance_dict