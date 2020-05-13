'''
1. Create a Box class, representing rectangular 3D boxes. The boxes can be any size and can be located anywhere in 3D space, but in this simple version their orientations are fixed so that their edges are always aligned with/parallel to coordinate system axes. You class must implement all the methods below:
__init__(self, centerX = 0.0, centerY = 0.0, centerZ = 0.0, width = 1.0, height = 1.0, depth = 1.0)
setCenter(self, x, y, z)
setWidth(self, width)
setHeight(self, height)
setDepth(self, depth)
volume(self)
surfaceArea(self)
overlaps(self, otherBox). box1.overlaps(box2) should return True if the two 3D boxes touch/intersect at all, even they just touch exactly at their edges or corners. (Think of boxes as filled/solid objects so that if a box fully contains another, they are also considered to be overlapping.)
isInside(self, otherBox). box1.isInside(box2) should return True if no point of box 1 is outside or even on the boundary of box2
__repr__(self)
'''

class Box:
    def __init__(self, centerX = 0.0, centerY = 0.0, centerZ = 0.0, width = 1.0, height = 1.0, depth = 1.0):
        self.centerX = centerX
        self.centerY = centerY
        self.centerZ = centerZ
        self.width = width
        self.height = height
        self.depth = depth
    def setCenter(self, x, y, z):
        self.centerX = x
        self.centerY = y
        self.centerZ = z
    def setWidth(self, width):
        self.width = width
    def setHeight(self, height):
        self.height = height
    def setDepth(self, depth):
        self.depth = depth
    def volume(self):
        return self.height * self.width * self.depth
    def surfaceArea(self):
        xByY = self.height * self.width
        xByZ = self.depth * self.width
        zByY = self.depth * self.height
        return xByY * 2 + xByZ * 2 + zByY * 2
    def __repr__(self):
        return (f'<Box with center at ({self.centerX},{self.centerY},{self.centerZ}) with width of {self.width} height of {self.height} and depth of {self.depth}.>')
    def overlaps(self, otherBox):
        centerX1 = self.centerX
        centerY1 = self.centerY
        centerZ1 = self.centerZ  
        centerX2 = otherBox.centerX
        centerY2 = otherBox.centerY
        centerZ2 = otherBox.centerZ
        if abs(centerX1 - centerX2) > (self.width/2 + otherBox.width/2):
            return False
        elif abs(centerY1 - centerY2) > (self.height/2 + otherBox.height/2):
            return False
        elif abs(centerZ1 - centerZ2) > (self.depth/2 + otherBox.depth/2):
            return False
        else:
            return True
    def isInside(self, otherBox):
        if self.centerX + self.width/2 >= otherBox.centerX + otherBox.width/2 or self.centerX - self.width/2 <= otherBox.centerX - otherBox.width/2:
            return False
        elif self.centerY + self.height/2 >= otherBox.centerY + otherBox.height/2 or self.centerY - self.height/2 <= otherBox.centerY - otherBox.height/2:
            return False
        elif self.centerZ + self.depth/2 >= otherBox.centerZ + otherBox.depth/2 or self.centerZ - self.depth/2 <= otherBox.centerZ - otherBox.depth/2:
            return False
        else:
            return True


'''
2. Create a NimGame class that implements a two-player Nim-style game (see http://en.wikipedia.org/wiki/Nim for details of several variants). The game starts with one or more "heaps" of one or more items (we'll call them balls). Players take turns removing one or more balls from any heap. The player who removes the last item wins . You can play an interactive on-line version of the game here: here. Note that the on-line version is slightly different in that the player who removes the last item loses.

For this assignment, we'll keep things simple. Assume there's one human player playing against the computer and that the human always goes first.
To create the NimGame class, implement at least three methods:
an __init__ method, with one argument, a list specifying the number of balls in each heap initially
a __repr__ method that will print a nice human readable representation of the game state.
a remove method, with two arguments specifying how many balls the human player wishes to remove and the heap from which to remove them. This method should check that the specified number of balls and specified heap are valid. If the input is not valid, print an appropriate message but do not modify the game state. If the input is valid, remove the balls, and check whether or not the game is over/the player has won. If the game is not over, the method should then automatically select a (legal) number of balls for the computer to remove from some heap, either randomly or through a "smart" strategy, and it should update the game state accordingly (and check whether the game is over/computer has won). Note: you might want to add an additional internally-used method, gameOver, that returns True or False based on the current game state.
'''
import random 
class NimGame:
    def __init__(self, heapList):
        self.heapList = heapList
    def __repr__(self):
        retstr = ''
        for i in range(0, len(self.heapList)):
            heapNum = i + 1
            ballsInHeap = self.heapList[i] * '0 '
            retstr += f"Heap{heapNum}: {ballsInHeap}\n"
    def getName(self):
        retstr = ''
        for i in range(0, len(self.heapList)):
            heapNum = i + 1
            ballsInHeap = self.heapList[i] * '0 '
            retstr += f"Heap{heapNum}: {ballsInHeap}\n"
        return retstr
    def gameOver(self):
        gameGoing = True
        oneInHeap = 0
        zeroInHeap = 0
        for i in range(0,len(self.heapList)):
            if self.heapList[i] == 1:
                oneInHeap += 1
            if self.heapList[i] == 0:
                zeroInHeap += 1
        if oneInHeap == 1 and zeroInHeap == len(self.heapList) - 1:
            gameGoing = False
        return gameGoing

    def computerRemove(self):
        foundStack = False
        while not foundStack:
            randomStackindex = random.randint(0, len(self.heapList)-1)
            randomStack = self.heapList[randomStackindex]
            if randomStack != 0:
                randomRemove = random.randint(1, randomStack)
                foundStack = True
        self.heapList[randomStackindex] = randomStack - randomRemove
        print()
        print(f'Computer removed {randomRemove} ball(s) from heap {randomStackindex + 1}')
        
    def remove(self, howMany, whichStack):
        if self.heapList[whichStack-1] >= howMany:
            self.heapList[whichStack-1] = self.heapList[whichStack-1] - howMany
            print(f'You have removed {howMany} from stack {whichStack}.')
        else:
            print("There are not enough balls to remove from that stack.")
            return
        zeroHeaps = 0
        for i in range(0,len(self.heapList)):
            if self.heapList[i] == 0:
                zeroHeaps += 1
        if zeroHeaps == len(self.heapList):
            print('You took the last ball(s). You loose.')
            return
        gameState = self.gameOver()
        if gameState == False:
            print('There is one ball left. You win!')
            return
        self.computerRemove()
        zeroHeaps = 0
        for i in range(0,len(self.heapList)):
            if self.heapList[i] == 0:
                zeroHeaps += 1
        if zeroHeaps == len(self.heapList):
            print('The computer took the last ball(s). You win!')
        gameState = self.gameOver()
        if gameState == False:
            print('There is only one ball left. You have lost.')
        print()
        print('\nCurrent game board:')
        retstr = ''
        for i in range(0, len(self.heapList)):
            heapNum = i + 1
            ballsInHeap = self.heapList[i] * '0 '
            retstr += f"Heap{heapNum}: {ballsInHeap}\n"
        print(retstr)

'''
3. Add one additional subclass of Animal, including at least one new method, to
the code from animals.py.  
'''
class Animal ():
    
    numAnimals = 0

    def __init__ (self, name = 'NoName', numLegs = 0):
        self.name = name
        self.numLegs = numLegs
        Animal.numAnimals = Animal.numAnimals + 1
        self.id = Animal.numAnimals

    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def getNumLegs(self):
        return self.numLegs
   
    def speak(self):
        print("...")

    def __repr__(self):
        return ('<{} the animal. ID:{}>'.format(self.name, self.id))

class Cat(Animal):
    def __init__(self, name = 'noname', furColor = 'unknown'):
        Animal.__init__(self, name, 4)
        self.color = furColor
    
    def speak(self):
        print('meow')

    def getFurColor(self):
        return self.color

    def __repr__(self):
        return ('<{} the {} cat. ID: {}>'.format(self.name, self.color, self.id))

class Dog(Animal):
    
    def __init__(self, name = 'rover'):
        Animal.__init__(self, name, 4)
    
    def speak(self):
        print('woof')
        
    def fetch(self):
        print("I'm fetching ...")

    def __repr__(self):
        return '<{} the dog. ID:{}>'.format(self.name, self.id)
    
class Cow(Animal):
    def __init__(self, name='Bessy', breed = 'Angus'):
        Animal.__init__(self, name, 4)
        self.breed = breed
    def speak(self):
        print('Moo!')
    def getMilk(self):
        if self.breed == 'Angus':
            print('I am not a dairy cow!')
        else:
            print('I have milk for you!')
    def getName(self):
        print(f"Hi! My name is {self.name}")
    def __repr__(self):
        return f'<{self.name} the {self.breed} cow. ID:{self.id}>'