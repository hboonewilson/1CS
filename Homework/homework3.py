def q1(n):
    if n == 0:
        return []
    else:
        return q1(n-1) + [n**2] + q1(n-1)

def q2(lis, n):
    if lis == []:
        return 0
    else:
        if len(lis[0]) < n:
            return q2(lis[1:], n) + 1
        else:
            return q2(lis[1:], n)

def helperq3(items):
    itemlis = []
    for item in items:
        if item == []:
            itemlis.append(None)
        elif type(item) == list:
            itemlis += helperq3(item)
        else:
            length = len(items)
            itemlis.append(item)
            itemlis.append([length])
    return itemlis

def q3(item1, item2):
    if type(item1) != list or type(item2) != list:
        if type(item1) == type(item2):
            return True
        else:
            return False
    verify = True
    unnested1 = helperq3(item1)
    unnested2 = helperq3(item2)
    if len(item1) == len(item2):
        for i in range(0, len(unnested1)):
            if type(unnested1[i]) == int and type(unnested2[i]) == float:
                pass
            elif type(unnested1[i]) == float and type(unnested2[i]) == int:
                pass
            else:
                if type(unnested1[i]) == list and type(unnested2[i]) == list:
                    if unnested1[i] != unnested2[i]:
                        verify = False
                else:
                    if type(unnested1[i]) != type(unnested2[i]):
                        verify = False
    else:
        verify = False
    return verify

def q4(aString):
    if len(aString) == 1:
        #if len of aString is 1, return the input string
        return [aString]
    #create a list (liss to return for each recursion call
    liss = []
    #for each permutation from recursion call: enter stack...
    for lis in q4(aString[1:]):
        #iterate through each indicy and place leter in new spot
        for i in range(len(aString)):
            liss.append(lis[:i] + aString[0] + lis[i:])
    #return liss for next recursion call
    return liss
