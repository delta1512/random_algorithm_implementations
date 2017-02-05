import random
import time
import os

#Initialise the area for the tiles
global Area
Area = []
global SizeOfAreax, SizeOfAreay
SizeOfAreax, SizeOfAreay = 20, 20 #X and Y of the size of the area

#Define a tile
class Tile:
    fillCount = 0 #Variable to count tiles that have been filled
    def __init__(self):
        self.contents = 0 #Variable to print
        self.filled = False #Has the tile been discovered?
    def discover(self): #Discover function
        self.contents = 1
        self.filled = True
        Tile.fillCount += 1
    def retcontents(self): #Return contents
        return self.contents
    def fillStatus(self): #Return discovery status
        return self.filled
    def changeContents(self, char): #Change the contents
        self.contents = str(char)

#Initialise area array
for x in range(0, SizeOfAreax):
    new = []
    for y in range(0, SizeOfAreay):
        new.append(Tile())
    Area.append(new)

#Prints the contents of each cell
def Render_Area():
    bitmap = ''
    #For loop iterates differently so that it flips the output
    for y in range(SizeOfAreay-1, -1, -1): 
        for x in range(0, SizeOfAreax):
            bitmap = bitmap + str(Area[x][y].retcontents())
        bitmap = bitmap + '\n'
    print(bitmap)

#Checks if the adjacent tiles have been discovered and returns the ones that are not
def Check_Neighbours(x, y):
    neighbours = []
    if 0 <= x < SizeOfAreax-1:
        if not Area[x+1][y].fillStatus():
            neighbours.append([x+1, y])
    if 0 < x <= SizeOfAreax-1:
        if not Area[x-1][y].fillStatus():
            neighbours.append([x-1, y])
    if 0 <= y < SizeOfAreay-1:
        if not Area[x][y+1].fillStatus():
            neighbours.append([x, y+1])
    if 0 < y <= SizeOfAreay-1:
        if not Area[x][y-1].fillStatus():
            neighbours.append([x, y-1])
    return neighbours

#Picks a randon item in a set
def Pick_Random(set):
    rand = random.randint(0, len(set)-1)
    return set[rand]

#Sets the current X and Y variables to random values within the area
Currentx, Currenty = random.randint(0, SizeOfAreax-1), random.randint(0, SizeOfAreay-1)
Area[Currentx][Currenty].discover() #Discover the selected values
stack = [] #Initialise the stack
Area[Currentx][Currenty].changeContents('_') #Set a different character to show the current tile
while Tile.fillCount < SizeOfAreax * SizeOfAreay: #While there are still undiscovered tiles
    Area[Currentx][Currenty].changeContents(1) #Change character to the default "discovered"
    if len(Check_Neighbours(Currentx, Currenty)) > 0: #If there are neighbours
        newCurrent = Pick_Random(Check_Neighbours(Currentx, Currenty))
        stack.append(newCurrent) #Push chosen neighbour onto the stack
        Currentx, Currenty = newCurrent[0], newCurrent[1] #Make it the current tile
        Area[Currentx][Currenty].discover() #Set it as discovered
    elif len(stack) != 0: #If there are no neighbours and the stack is not empty
        back = stack.pop() #Get the previous tile
        Currentx, Currenty = back[0], back[1] #Set it as current
    Area[Currentx][Currenty].changeContents('_') #Set a different character to show the current tile
    os.system('cls' if os.name == 'nt' else 'clear')
    Render_Area() #Print the contents of the area to the terminal
    time.sleep(0.1) #Speed of the processing (So you can actually see it run)
Area[Currentx][Currenty].changeContents(1) #Finish by setting current as discovered
Render_Area()
