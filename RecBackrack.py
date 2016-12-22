import random
import time

global Area
Area = []
global SizeOfAreax, SizeOfAreay
SizeOfAreax, SizeOfAreay = 20, 20

class Tile:
    fillCount = 0
    def __init__(self):
        self.contents = 0
        self.filled = False
    def discover(self):
        self.contents = 1
        self.filled = True
        Tile.fillCount += 1
    def retcontents(self):
        return self.contents
    def fillStatus(self):
        return self.filled
    def changeContents(self, icon):
        self.contents = str(icon)

for x in range(0, SizeOfAreax):
    new = []
    for y in range(0, SizeOfAreay):
        new.append(Tile())
    Area.append(new)

def Render_Area():
    bitmap = ''
    for y in range(SizeOfAreay-1, -1, -1):
        for x in range(0, SizeOfAreax):
            bitmap = bitmap + str(Area[x][y].retcontents())
        bitmap = bitmap + '\n'
    print(bitmap)

def Check_Neighbours(x, y):
    neighbours = []
    if 0 < x < SizeOfAreax-1:
        if not Area[x-1][y].fillStatus():
            neighbours.append([x-1, y])
        if not Area[x+1][y].fillStatus():
            neighbours.append([x+1, y])
    elif x == 0:
        if not Area[x+1][y].fillStatus():
            neighbours.append([x+1, y])
    else:
        if not Area[x-1][y].fillStatus():
            neighbours.append([x-1, y])
    if 0 < y < SizeOfAreay-1:
        if not Area[x][y-1].fillStatus():
            neighbours.append([x, y-1])
        if not Area[x][y+1].fillStatus():
            neighbours.append([x, y+1])
    elif y == 0:
        if not Area[x][y+1].fillStatus():
            neighbours.append([x, y+1])
    else:
        if not Area[x][y-1].fillStatus():
            neighbours.append([x, y-1])
    return neighbours

def Pick_Random(set):
    rand = random.randint(0, len(set)-1)
    return set[rand]

initx, inity = random.randint(0, SizeOfAreax-1), random.randint(0, SizeOfAreay-1)
Area[initx][inity].discover()
Currentx, Currenty = initx, inity
stack = []
Area[Currentx][Currenty].changeContents('_')
while Tile.fillCount < SizeOfAreax * SizeOfAreay:
    Area[Currentx][Currenty].changeContents(1)
    if len(Check_Neighbours(Currentx, Currenty)) > 0:
        newCurrent = Pick_Random(Check_Neighbours(Currentx, Currenty))
        stack.append(newCurrent)
        Currentx, Currenty = newCurrent[0], newCurrent[1]
        Area[Currentx][Currenty].discover()
    elif len(stack) != 0:
        back = stack.pop()
        Currentx, Currenty = back[0], back[1]
    Area[Currentx][Currenty].changeContents('_')
    Render_Area()
    time.sleep(0.1)
Area[Currentx][Currenty].changeContents(1)
Render_Area()
