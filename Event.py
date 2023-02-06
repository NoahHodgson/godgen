import God
import Hero
import Location

class Event:
    raw_event: str = ""
    characters: list = []
    filled_event: str = ""
    condition: tuple = ()

    # limiting 3 characters per event for now
    def build_event(self):
        cloned_event = self.raw_event
        for string in cloned_event:
            if string == 'CHARACTER0':
                string = self.characters[0]
            elif string == 'CHARACTER1':
                string = self.characters[1]
            elif string == 'CHARACTER2':
                string = self.characters[2]
        return cloned_event

    def __init__(self, raw, chars, filled, condition):
        self.raw_event = raw
        self.characters = chars
        self.filled_event = self.build_event()
        self.condition = condition 
