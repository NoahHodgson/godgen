import Location
import json
import random

BASIC_RANGE = [0,1,2,3,4,5]
SIZE = 9

def Print_Terrain(grid):
    for i in range(SIZE):
        for j in range(SIZE):
            # inverting j and i so the poles are north and south
            print(grid[j][i].biome, end=";  ")
        print()

def Print_Emoticon(grid):
    for i in range(SIZE):
        for j in range(SIZE):
            # inverting j and i so the poles are north and south
            if grid[j][i].temperature == -1:
                print('⬛', end=' ')
            elif grid[j][i].temperature == 0:
                print('⬜', end=' ')
            elif grid[j][i].biome == 'water':
                print('🟦', end=' ')
            elif grid[j][i].temperature == 1:
                print('⬜', end=' ')
            elif grid[j][i].elevation > 3:
                print('🔺', end=' ')
            elif grid[j][i].vegitation > 3:
                print('🌳', end=' ')
            elif grid[j][i].temperature > 3 or grid[j][i].vegitation <= 1:
                print('🟨', end=' ')
            else:
                print('🟩', end=' ')
        print()
# def Print_Civ(grid):

# def Print_All_Map(grid):

# def Add_Pop(grid)

def Ocean_Generator(grid, flood_limit):
    for i in range(SIZE):
        if (flood_limit <= 0):
            break
        for j in range(SIZE):
            if grid[j][i].elevation == 0 and grid[j][i].temperature != 0:
                flood = random.choice([False, True, True, True, True])
                if flood:
                    grid[j][i].submerge()
                    flood_limit-= 1
            elif grid[j][i].elevation == 1 and grid[j][i].temperature != 0:
                flood = random.choice([False, True, True, True])
                if flood:
                    grid[j][i].submerge()
                    flood_limit-= 1
            elif grid[j][i].elevation == 2 and grid[j][i].temperature != 0:
                flood = random.choice([False, True])
                if flood:
                    grid[j][i].submerge()
                    flood_limit-= 1

            if (flood_limit <= 0):
                break
    return flood_limit

# climate is based on two poles and equator
def Basic_Polar_World_Generator():
    last_veg = -1
    last_height = -1
    grid=[[None]*SIZE for o in range(SIZE)]
    for i in range(SIZE):
        for j in range(SIZE):
            if last_veg != -1:
                NEW_RANGE = BASIC_RANGE.copy()
                NEW_RANGE.extend([last_veg, last_veg])
                if last_veg != 0 and last_veg != 5:
                    NEW_RANGE.extend([last_veg+1, last_veg-1])
                veg = random.choice(NEW_RANGE)
            else:
                veg = random.choice(BASIC_RANGE)

            if last_height != -1:
                NEW_RANGE = BASIC_RANGE.copy()
                NEW_RANGE.extend([last_height, last_height])
                if last_height != 0 and last_height != 5:
                    NEW_RANGE.extend([last_height+1, last_height-1])
                height = random.choice(NEW_RANGE)
            else:
                height = random.choice(BASIC_RANGE)

            if j == 0 or j == SIZE-1:
                temp = 0
            elif j == 1 or j == SIZE - 2:
                temp = random.choice([1, 2])
                if height > 3:
                    temp-=1
            elif j == 2 or j == SIZE - 3:
                temp = random.choice([2, 3])
                if height > 3:
                    temp-=1
            else:
                temp = random.choice([3, 3, 4, 4, 5])
                if height > 3:
                    temp-=1

            # creation function call
            grid[i][j] = Location.Location(i, j, temp, height, veg)
            last_veg = veg
            last_height = height
            


    Ocean_Generator(grid, 10)
    Print_Emoticon(grid)
    return grid

# climate of the world is generated similar to terrain and vegitation
def Basic_Nonpolar_World_Generator():
    grid=[[]]
    return grid

# generate planet with Islands and lots of water
def Basic_Island_World_Generator():
    grid=[[]]
    return grid

# generate world with square planets and void
def Basic_Galactic_World_Generator():
    grid=[[]]
    return grid

# generate world that uses z-levels for multiple planes of existence
""" 
this sounds painful
def Basic_MultiPlanar_Generator():
    grid=[[]]
    return grid
"""
# testing area
Basic_Polar_World_Generator()
