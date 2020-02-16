#Write function modifyString(origString, charsToReplace, count) that takes as input 
#a string origString, a string charsToReplace, and a positive integer count, and 
#returns a new string such that each character in origString that occurs in 
#charsToReplace is replaced by n consecutive copies of that character 
#(with the same case as in the original).
def modifyString(origString, charsToReplace, count):
    retstr = ''
    for let in origString:
        if let.lower() in charsToReplace.lower():
            retstr += (let * count)
        else:
            retstr += let
    return retstr

#Write a function, q2(inputString, minLetter), that takes as input a string of 
#letters and returns six things: the lexicographically smallest letter (z/Z > y/Y > ... > a/A) 
#greater or equal to minLetter, the smallest index at which that letter occurs, 
#the third smallest letter greater than minLetter, the smallest index at which 
#that letter occurs, the most common letter, and how many times the most common 
#letter occurs. The third smallest letter must be distinct from the second smallest 
#which must be distinct from the smallest. E.g. 'b' is the second smallest and 'c' 
#is the third smallest in 'ababdc'
def checkForLet(letter, string):
    '''Helper function that returns how many times a ch is in a string.'''
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count

def q2(inputString, minLetter): 
    inputString = inputString.lower()
    
    
    #find the leter tha occurs most frequently with the helper function checkForLet()
    largestlet = None
    maxtimes = 0
    for char in inputString:
        
        #for each character in the string use checkForLet to return how many times
        #that character was present in a string 
        timeschar = checkForLet(char, inputString)
        
        #if there is no largest letter yet or the higest frequency letter 
        #is smallert than new frequency
        if largestlet == None or maxtimes < timeschar:
            #reset the top variables
            maxtimes = timeschar
            largestlet = char    
        if timeschar == maxtimes:
            if largestlet > char:
                maxtimes = timeschar
                largestlet = char

    #first smallest
    winner = None
    index = 0
    winning_in = None
    while index < len(inputString):
        let = inputString[index]
        if let >= minLetter:
            if winner == None or let < winner:
                winner = let
                winning_in = index
        index += 1
        
    #change names of variables to understand them later
    first_small = winner
    first_s_index = winning_in
    
    
    
    #find second smallest
    #second smallest doesn't need index just it's value
    sec_sm = None
    index = 0
    for let in inputString:
        if first_small != None and let > first_small:
            if sec_sm == None or sec_sm > let:
                sec_sm = let
      
    third = None
    thindex = None
    index = 0
    #find third smallest ch
    while index < len(inputString):
        let = inputString[index]
        if sec_sm != None and let > sec_sm:
            if third == None or let < third:
                third = let
                thindex = index
        index += 1
    return first_small, first_s_index, third, thindex, largestlet, maxtimes
            
    
def q3a(string1, string2):
    '''Implement function q3a(string1, string2) so that it returns True if the input strings are the same length and differ at exactly one character position, and returns False otherwise. For example, q3a("bat", "bet") should return True while q3a("art", "rat") and q3a("art", "ran") should both return False.'''
    difindex = 0
    if len(string1) != len(string2):
        return False
    x = 0
    while x < len(string1):
        if string1[x] != string2[x]:
            difindex += 1
        x += 1
    if difindex == 1:
        return True
    else:
        return False 

def q3b(string1, string2):
    ''' Implement function q3b(string1, string2) so that it returns a list of the indices, in increasing order, at which string1 and string2 have identical characters. That is, index i should be in the returned list if the ith character of string1 and string2 are the same. For example, q3b("cba", "cb") should return [0, 1] and q3b("bbcz", "Bbxzf") should return [1, 3].'''
    retlis = []
    x = 0
    if len(string1) < len(string2):
        smallerstr = len(string1)
    else:
        smallerstr = len(string2)
    while x < smallerstr:
        if string1[x] == string2[x]:
            retlis += [x]
        x += 1
    return retlis

def q4(L, goalX, goalY):
    ''' Implement function, q4(L, goalX, goalY), that takes a non-empty list, L, of [x,y] pairs, and two goal numbers, and returns tuple (closestXY, XorY) where closestXY is the item from L whose x distance from goal X or whose y distance from goalY is the minimum among all distances, and XorY is 'x' if x distance is minimized and 'y' otherwise. You may assume there is a unique answer. Note: You may not use built-in min or max functions. q4([[4, 4], [10, 10]], 1, 8) should return ([10,10], 'y')'''
    minimum = None
    xory = None
    thelis = None
    for lis in L:

        xdis = goalX - lis[0]
        ydis = goalY - lis[1]
        if xdis < 0:
            xdis = xdis * -1
        if ydis < 0:
            ydis = ydis * -1
        if ydis < xdis:
            smalldis = ydis
            xissmal = False
        else:
            smalldis = xdis
            xissmal = True

        if minimum == None or minimum > smalldis:
            minimum = smalldis
            thelis = lis
            if xissmal:
                xory = 'x'
            else:
                xory = 'y'
    return thelis, xory
            
def q5(L):
    '''Implement function q5(L) that takes as input a (possibly empty) list of (possibly empty) lists of numbers and returns a three-element list. The first element is a list of the sums of corresponding lists in L, the second element is the number of lists in L that contain more positive than negative values, and the third element in the minimum value among all items in all lists (or None if there is no minimum). Note: you may NOT use Python's 'sum' or 'min' function (instead,compute sums and min within a loop or loops.) >>> q5([[1, 2, 2], [3]]) == [[5, 3], 2, 1] >>> q5([[0, 1, 0], [], [-1, 100]]) == [[1, 0, 99], 1, -1]'''
    poslists = 0
    sumlis = []
    smallest = None
    for lis in L:
        posi = 0
        neg = 0
        ans = 0
        for element in lis:
            if smallest == None or smallest > element:
                smallest = element
            ans += element
            if element < 0:
                neg += 1
            elif element > 0:
                posi += 1
        sumlis += [ans]
        if posi > neg:
            poslists += 1
    return sumlis, poslists, smallest
