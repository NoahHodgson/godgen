import ClassDefinitions.God as God
import ClassDefinitions.Hero as Hero
import ClassDefinitions.Location as Location

class Society:
    name: str = None
    members: list = []
    worships: list = []

    allied_to: list = []
    enemy_of: list = []
    own: list = []

    is_alive = True
    events = []

    def __init__(self, nm, members, worships, allies, enemies, own, events):
        self.name = nm
        self.members = members
        self.worships = worships
        self.allied_to = allies
        self.enemy_of = enemies
        self.own = own
        self.events = events
