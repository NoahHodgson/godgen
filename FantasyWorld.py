class FantasyWorld:
    name = None
    good_evil_score = None
    max_world_age = None
    fantasy_level = None
    gods = []
    pantheon = []
    events = []
    races = []
    civs = []

    def __init__(self, name, ge, mwa, fl):
        self.name = name
        self.good_evil_score = ge
        self.max_world_age = mwa
        self.fantasy_level = fl

