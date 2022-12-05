import ClassDefinitions.God as God
import ClassDefinitions.Hero as Hero
import ClassDefinitions.Location as Location

class Society:
    name: str = None
    members: list = []
    worships: list = []
    tech_age: str = None

    allied_to: list = []
    enemy_of: list = []
    own: list = []

    is_alive = True
    events = []

    def __init__(self, nm, members, worships, age, allies, enemies, own, events):
        self.name = nm
        self.members = members
        self.worships = worships
        self.tech_age = age
        self.allied_to = allies
        self.enemy_of = enemies
        self.own = own
        self.events = events
