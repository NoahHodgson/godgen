#Fantaworld Building-Up by Noah Hodgson 2019-2020
#Goal is to convert the proof of concept code from the god generator into the fantasy world generator

#Version swaps over from dictionaries to classes.

#stores values needed for creating and using god's in order for them to interact with (evenetual) world

class FantasyGod:
    name = None
    sphere = None
    gender = None
    god_of1 = None
    god_of2 = None
    involvement_level = None
    has_angel_like = None
    has_pantheon = None
    has_incarnate = None
    appearance = {
        "base": None,
        "trait1": None,
        "trait2": None,
        "trait3": None,
        "countenance":None
    }

    def printGod(self):
        if(self.sphere == "force"):
            print("This is " + self.name + ", the force of " + self.god_of1 + " and " + self.god_of2 + ". ")
        elif(self.sphere == "eldritch"):
            print("This is " + self.name + ", the ancient one, known for " + self.god_of1 + " and " + self.god_of2 + ". ")
        else:
            print("This is " + self.name + ", god of " + self.god_of1 + " and " + self.god_of2 + ". ")
        #appearance will go here.
        if(self.gender == "male"):
            print("He has ", end = '')
        elif (self.gender == "female"):
            print("She has ", end = '')
        elif(self.gender == "force"):
            print("It has ", end = '')
        else:
            print("They have ", end = '')
        #^^^Will be used in appearance as well^^^
        #involve-level check
        if(self.involvement_level == 0):
            print("no interaction with the world. ")
        elif(self.involvement_level > 0 and self.involvement_level <= 3):
            print("little interaction with the world. ")
        elif(self.involvement_level > 3 and self.involvement_level<= 6):
            print("has decent interaction with the world. ")
        elif(self.involvement_level > 6 and self.involvement_level <= 9):
            print("has a lot of interaction with the world. ")
        elif(self.involvement_level == 10):
            print("lives among the people of the world. ")
        else:
            print("EXIT ERROR. YOU FORGOT HOW PYTHON WORKS")
        
        #update to include sphere cases
        if(self.has_angel_like == True):
            print(self.name + " has angels. ")
        else:
            print(self.name +" does not have angels. ")
        
        #has pantheon (pan might be a passed in argument)
        if(self.has_pantheon == True):
            print(self.name + " is part of a pantheon. ")
        else:
            print(self.name +" is not part of a pantheon. ")

        #incarnates
        if(self.has_incarnate == True):
            print(self.name + " has an incarnate form. ")
        else:
            print(self.name +" does not have incarnate form. ")

        print(self.appearance) ###Temporary
        
        print("This is " + self.name + "'s overview.")

    #current constructor - missing appearance
    def __init__(self, nm, sphr, gndr, g_of1, g_of2, inv_lvl, has_ang, has_pan, has_inc, appearance_dict):
        self.name = nm
        self.sphere = sphr
        self.gender = gndr
        self.god_of1 = g_of1
        self.god_of2 = g_of2
        self.involvement_level = inv_lvl
        self.has_angel_like = has_ang
        self.has_pantheon = has_pan
        self.has_incarnate = has_inc
        self.appearance = appearance_dict

#This part is the traditional Hades test.
hades_app = {"trait1": "has staff", "trait2": "dark hair", "trait3":"shaggy beard"}
Hades = FantasyGod("Hades", "neutral", "male", "death", "wealth", 3, False, True, False, hades_app)
Hades.printGod()



    

