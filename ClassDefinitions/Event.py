import ClassDefinitions.God as God
import ClassDefinitions.Hero as Hero
import ClassDefinitions.Location as Location

class Event:
    raw_event: str = ""
    characters: list = []
    filled_event: str = ""
    condition: tuple = ()


    def __init__(self, raw, chars, filled, condition):
        self.raw_event = raw
        self.characters = chars
        self.filled_event = filled
        self.condition = condition 
