# CS 1210, Spring 2020
# Discussion section 7, April 8-10

# DISCUSSION SECTION WORK:
#

# Download this file, ds7.py and also stack.py and cirle.py
#
# 1. After studying the Stack class and testStack() functions in stack.py
#    complete the Queue class below (and test it with the testQueue function)
#
# 2. Afer studying and testing the Circle class in circle.py,
#    complete the Rectangle class below (and test it with
#    the testRectangle function)
#
# 3. SUBMIT THIS FILE TO ICON.
#
#
# NOTE: you may certainly add more tests to the test functions if you want!!

#####

# 1. Complete the Queue class (following the style of the Stack class)
#
# A queue is similar to a stack but a bit different.
#
# A queue is a collection of items supporting three operations:
#   - enqueue (item): add item to the “front” of the queue
#   - dequeue(): removes the “last” item from the queue
#                 (the one that’s been in the queue the longest) and returns it
#   - size(): returns the number of items currently in the queue
#
# Note: stacks are “LIFO” (last-in-first-out)
#       while queues are “FIFO” (first-in-first-out)

class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        temp = self.items[:]
        self.items = [item] + temp
    def dequeue(self):
        #if len(self.items) == 0:    ##Works##
            #return None
        last = self.items[-1]
        self.items = self.items[:-1]
        return last
    def size(self):
        return (len(self.items))


def testQueue():
    q = Queue()
    print("Created an empty Queue")
    print("Size is now: {}".format(q.size()))
    print("Enqueue-ing: 3, then 'hi', then 99")
    q.enqueue(3)
    q.enqueue("hi")
    q.enqueue(99)
    q.items
    print("Size is now: {}".format(q.size()))
    print("Dequeue-ing ...")
    print(q.dequeue())
    print(q.items)
    print("Size is now: {}".format(q.size()))
    print("Dequeue-ing ...")
    print(q.dequeue())
    print(q.items)
    print("Size is now: {}".format(q.size()))
    print("Enqueue-ing: [1,2]")
    q.enqueue([1,2])
    print(q.items)
    print("Size is now: {}".format(q.size()))
    print("Dequeue-ing ...")
    print(q.dequeue())
    print(q.items)
    print("Size is now: {}".format(q.size()))
    print("Dequeue-ing ...")
    print(q.dequeue())
    print(q.items)
    print("Size is now: {}".format(q.size()))
    print(q.dequeue())
    print(q.items)
    print("Size is now: {}".format(q.size()))


# 2. Complete the Rectangle class (following the style of the Circle class) 

import math

class Rectangle:
    def __init__(self, centerX = 0.0, centerY = 0.0, width = 0.0, height = 0.0):
        self.centerX = centerX
        self.centerY = centerY
        self.width = width
        self.height = height
    
    def __repr__(self):
        return f"<Rectangle with width of {self.width} and height of {self.height} and center at ({self.centerX},{self.centerY})>"
       
    def setCenter(self, x, y):
        self.centerX, self.centerY = x, y
    
    def setWidth(self, width):
        self.width = width
    
    def setHeight(self, height):
        self.height = height

    def area(self):
        return self.width * self.height
        
    def perimeter(self):
        return self.width * 2 + self.height * 2
   
    #
    # the intersects method should return True if the two rectangles
    # touch/intersect at all (even they just touch exactly at their edges or
    # corners). Note: think carefully about how to do this test. Sketching
    # some pictures can help you analyze the possibilities.
    #
    def intersects(self, otherRectangle):
        l1 = [self.centerX - self.width/2, self.centerY + self.height/2]
        r1 = [self.centerX + self.width/2, self.centerY - self.height/2]
        
        l2 = [otherRectangle.centerX - otherRectangle.width/2, otherRectangle.centerY + otherRectangle.height/2]
        r2 = [otherRectangle.centerX + otherRectangle.width/2, otherRectangle.centerY - otherRectangle.height/2]
        
        if l1[0] > r2[0] or l2[0] > r1[0]:
            return False
        if l1[1] < r2[1] or l2[1] < r1[1]:
            return False
        else:
            return True
def testRectangle():
    rect1 = Rectangle(10.0, 5.0, 2.0, 1.0)
    print("Rectangle 1:", rect1)
    print("  area:", rect1.area(), "perimeter:", rect1.perimeter())
    rect2 = Rectangle(0, 0, 3.5, 2.5)
    print("Rectangle 2:", rect2)
    print("Rectangle 1 interects Rectangle 2:", rect1.intersects(rect2))
    rect1.setCenter(2.75, 0.0)
    print("After setting center of Rectangle 1 to (2.75, 0.0)")
    print("Rectangle 1 interects Rectangle 2:", rect1.intersects(rect2))
    rect1.setCenter(2.76, 0.0)
    print("After setting center of Rectangle 1 to (2.76, 0.0)")
    print("Rectangle 1 interects Rectangle 2:", rect1.intersects(rect2))
    rect1.setCenter(-2.75, 1.75)
    print("After setting center of Rectangle 1 to (-2.75, 1.75)")
    print("Rectangle 1 interects Rectangle 2:", rect1.intersects(rect2))
    print("After setting center of Rectangle 1 to (0,0)")
    rect1.setCenter(0.0, 0.0)
    print("Rectangle 1 interects Rectangle 2:", rect1.intersects(rect2))
    rect1.setCenter(10.0,0)
    print("After setting center of Rectangle 1 to (10.0, 0.0)")
    print("Rectangle 1 interects Rectangle 2:", rect1.intersects(rect2))   
    rect1.setWidth(20.0)  
    print("After setting width of Rectangle 1 to 20.0")
    print("Rectangle 1 interects Rectangle 2:", rect1.intersects(rect2))
    rect1.setCenter(0,-10)
    print("After setting center of Rectangle 1 to (0, -10.0)")
    print("Rectangle 1 interects Rectangle 2:", rect1.intersects(rect2))   
    rect1.setHeight(17.5)  
    print("After setting height of Rectangle 1 to 17.5")
    print("Rectangle 1 interects Rectangle 2:", rect1.intersects(rect2))    
