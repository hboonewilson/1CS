def middle(inList):
    return(inList[1:len(inList)-1])

def chop(inList):
    del inList[0]
    del inList[len(inList)-1]



# Understand the diffences between the four functions below!
#
# Try, in Python interpreter:
# >>> myList = [1,2,3]
# >>> bar(myList)
# >>> myList
# >>> myList = [1,2,3]
# >>> bar2(myList)
# >>> myList
# >>> myList = [1,2,3]
# >>> baz(myList)
# >>> myList
# >>> myList = [1,2,3]
# >>> baz2(myList)
# >>> myList

def bar(inList):
    x = inList[0] + 3
    middle(inList)
    inList = inList + inList + [x]
    return(inList)

def bar2(inList):
    x = inList[0] + 3
    inList = middle(inList)
    inList = inList + inList + [x]
    return(inList)

def baz(inList):
    x = inList[0] + 3
    chop(inList)
    inList = inList + inList + [x]
    return(inList)

def baz2(inList):
    x = inList[0] + 3
    inList[0] = 100
    inList = inList + inList + [x]
    return(inList)