# Single grid on the location
# A world is made up of a lot of these 

temperature_dict = {0:"glacial", 1:"cool", 2:"temperate", 3:"warm", 4:"hot", 5:"blazing",}
elevation_dict = {0:"flat", 1:"plains", 2:"plateau", 3:"hills", 4:"mountain", 5:"summit"}
vegitation_dict = {0:"wasteland", 1:"desert", 2:"sparse", 3:"lively", 4:"plentiful", 5:"dense"}

biome_dict = {
    '000':"", '001':"", '002':"", '003':"", '004':"", '005':"",
    '010':"", '011':"", '012':"", '013':"", '014':"", '015':"",
    '020':"", '021':"", '022':"", '023':"", '024':"", '025':"",
    '030':"", '031':"", '032':"", '033':"", '034':"", '035':"",
    '040':"", '041':"", '042':"", '043':"", '044':"", '045':"",
    '050':"", '051':"", '052':"", '053':"", '054':"", '055':"",
    '100':"", '101':"", '102':"", '103':"", '104':"", '105':"",
    '110':"", '111':"", '112':"", '113':"", '114':"", '115':"",
    '120':"", '121':"", '122':"", '123':"", '124':"", '125':"",
    '130':"", '131':"", '132':"", '133':"", '134':"", '135':"",
    '140':"", '141':"", '142':"", '143':"", '144':"", '145':"",
    '150':"", '151':"", '152':"", '153':"", '154':"", '155':"",
    '200':"", '201':"", '202':"", '203':"", '204':"", '205':"",
    '210':"", '211':"", '212':"", '213':"", '214':"", '215':"",
    '220':"", '221':"", '222':"", '223':"", '224':"", '225':"",
    '230':"", '231':"", '232':"", '233':"", '234':"", '235':"",
    '240':"", '241':"", '242':"", '243':"", '244':"", '245':"",
    '250':"", '251':"", '252':"", '253':"", '254':"", '255':"",
    '300':"", '301':"", '302':"", '303':"", '304':"", '305':"",
    '310':"", '311':"", '312':"", '313':"", '314':"", '315':"",
    '320':"", '321':"", '322':"", '323':"", '324':"", '325':"",
    '330':"", '331':"", '332':"", '333':"", '334':"", '335':"",
    '340':"", '341':"", '342':"", '343':"", '344':"", '345':"",
    '350':"", '351':"", '352':"", '353':"", '354':"", '355':"",
    '400':"", '401':"", '402':"", '403':"", '404':"", '405':"",
    '410':"", '411':"", '412':"", '413':"", '414':"", '415':"",
    '420':"", '421':"", '422':"", '423':"", '424':"", '425':"",
    '430':"", '431':"", '432':"", '433':"", '434':"", '435':"",
    '440':"", '441':"", '442':"", '443':"", '444':"", '445':"",
    '450':"", '451':"", '452':"", '453':"", '454':"", '455':"",
    '500':"", '501':"", '502':"", '503':"", '504':"", '505':"",
    '510':"", '511':"", '512':"", '513':"", '514':"", '515':"",
    '520':"", '521':"", '522':"", '523':"", '524':"", '525':"",
    '530':"", '531':"", '532':"", '533':"", '534':"", '535':"",
    '540':"", '541':"", '542':"", '543':"", '544':"", '545':"",
    '550':"", '551':"", '552':"", '553':"", '554':"", '555':"",
    'void':"", 'water':""
}

class Location:
    # physical locations
    x: int
    y: int
    z: int = -1 # not in use

    # descriptors, temp, veg, and elevation effect biome need function on update biome
    temperature:int
    elevation:int
    vegitation:int
    biome:str
    # water / void booleans.
    isUnderWater = False
    isVoid = False

    # info about the location
    owners = [] # stack, where the first owner is [0] and the current owner is [-1]
    population = 0
    # add location name later with a generator

    # use the dicts listed outside the class to compute the biome
    def compute_biome(self):
        biome = ""
        n_t = temperature_dict[self.temperature]
        n_e = elevation_dict[self.elevation]
        n_v = vegitation_dict[self.vegitation]
        key = n_t + n_e + n_v
        # change below, use later ==> biome = biome_dict[key]
        self.biome = n_t + ", " + n_e + ", " + n_v

    def submerge(self):
        self.biome = 'water'

    def voidify(self):
        self.temperature = -1
        self.vegitation = -1
        self.elevation = -1
        self.biome = 'void'

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
        self.temperature = temp
        self.elevation = elev 
        self.vegitation = veg
        self.compute_biome()
