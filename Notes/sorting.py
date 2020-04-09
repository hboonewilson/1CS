def sortOne(aList):
    for i in range(0, len(aList)):
       small = helperSortOne(aList, i)
       aList[i], aList[small] = aList[small], aList[i]
    return aList
def helperSortOne(aList, i):
    '''Find smallest value in portion of list from i to end'''
    smallest_v = None
    smallest_i = None
    for l in range(i, len(aList)):
        if smallest_v == None:
            smallest_v = aList[l]
            smallest_i = l
        elif smallest_v > aList[l]:
            smallest_i = l
            smallest_v = aList[l]
    return smallest_i

'''def insertionSort(aList):
    for i in range(0, len(aList)):
        pass
    pass
def helperInsertionSort(aList, i):
    for l in range(0, i):
        index = i - l - 1
        if aList[index] >= aList[i]:'''
            