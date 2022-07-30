# Single grid on the location
# A world is made up of a lot of these 

temperature_dict = {}
elevation_dict = {}
vegitation_dict = {}
biome_dict = {}

class Location:
    # physical locations
    x: int
    y: int
    z: int = -1 # not in use

    # descriptors, temp, veg, and elevation effect biome need function on update biome
    temperature:str
    elevation:str
    vegitation:str
    biome:str

    # info about the location
    owners = [] # stack, where the first owner is [0] and the current owner is [-1]
    population = 0
    # add location name later with a generator

    # use the dicts listed outside the class to compute the biome
    def compute_biome(t:str, e:str, v:str):
        biome = ""
        n_t = temperature_dict[t]
        n_e = elevation_dict[e]
        n_v = vegitation_dict[v]
        key = n_t + n_e + n_v
        biome = biome_dict[key]
        return biome

    def setPopulateSite(self, n_o:str, pop:int):
        if len(self.owners) != 0:
            if self.owners[-1] != n_o:
                self.owners.append(n_o)
        else:
            self.owners.append(n_o)
        self.pop = pop

    def getOwner(self):
        if len(self.owners) != 0:
            return self.owners[-1]   
        else:
            return "UNTAMED WILDS"

    def __init__(self, x, y, temp, elev, veg) -> None:
        self.x = x
        self.y = y
        self.temp = temp
        self.elevation = elev 
        self.vegitation = veg
        self.biome = self.compute_biome(temp, elev, veg)
