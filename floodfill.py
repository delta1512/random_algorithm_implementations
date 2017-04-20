import os
import random
from time import sleep

global Area
Area = []
global SizeOfAreax, SizeOfAreay
SizeOfAreax, SizeOfAreay = 20, 20

class Tile:
    fillCount = 0
    def __init__(self):
        self.contents = 0 #Variable to print
    def changeContents(self, char): #Change the contents
        self.contents = str(char)
        Tile.fillCount += 1

def Render_Area():
    bitmap = ''
    #For loop iterates differently so that it flips the output
    for y in range(SizeOfAreay-1, -1, -1):
        for x in range(0, SizeOfAreax):
            bitmap = bitmap + str(Area[x][y].contents)
        bitmap = bitmap + '\n'
    print(bitmap)

for x in range(0, SizeOfAreax):
    new = []
    for y in range(0, SizeOfAreay):
        new.append(Tile())
        if random.uniform(0, 10) < 2:
            new[y].changeContents(1)
    Area.append(new)

def flood_fill(tile_xy, replacement):
    if Area[tile_xy[0]][tile_xy[1]].contents == str(replacement):
        return
    Area[tile_xy[0]][tile_xy[1]].changeContents(replacement)
    print(Tile.fillCount)
    Render_Area()
    if 0 <= tile_xy[0] < SizeOfAreax-1:
        sleep(0.1)
        flood_fill([tile_xy[0]+1, tile_xy[1]], replacement)
    if 0 <= tile_xy[1] < SizeOfAreay-1:
        sleep(0.1)
        flood_fill([tile_xy[0], tile_xy[1]+1], replacement)
    if 0 < tile_xy[0] <= SizeOfAreax-1:
        sleep(0.1)
        flood_fill([tile_xy[0]-1, tile_xy[1]], replacement)
    if 0 < tile_xy[1] <= SizeOfAreay-1:
        sleep(0.1)
        flood_fill([tile_xy[0], tile_xy[1]-1], replacement)
    return True

rand_start = [random.randint(0, SizeOfAreax-1), random.randint(0, SizeOfAreay-1)]
Area[rand_start[0]][rand_start[1]].changeContents(0)
flood_fill(rand_start, 1)
