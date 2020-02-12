#Write function modifyString(origString, charsToReplace, count) that takes as input 
#a string origString, a string charsToReplace, and a positive integer count, and 
#returns a new string such that each character in origString that occurs in 
#charsToReplace is replaced by n consecutive copies of that character 
#(with the same case as in the original).
def modifyString(origString, charsToReplace, count):
    retstr = ''
    for let in origString:
        replace = False
        for ch in charsToReplace:
            if let == ch:
                replace = True
        if replace:
            let = let * count
        
        retstr += let
            
    return  retstr

#Write a function, q2(inputString, minLetter), that takes as input a string of 
#letters and returns six things: the lexicographically smallest letter (z/Z > y/Y > ... > a/A) 
#greater or equal to minLetter, the smallest index at which that letter occurs, 
#the third smallest letter greater than minLetter, the smallest index at which 
#that letter occurs, the most common letter, and how many times the most common 
#letter occurs. The third smallest letter must be distinct from the second smallest 
#which must be distinct from the smallest. E.g. 'b' is the second smallest and 'c' 
#is the third smallest in 'ababdc'
'''Make sure that the code is robust enough to evaluate if input string is empty 
or if there is no more letters larger than minLetter.'''
def checkForLet(letter, string):
    '''Helper function that returns how many times a ch is in a string.'''
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count

def q2(inputString, minLetter): 
    inputString = inputString.lower()
    
    if inputString == '':
        return None, None, None, None, None, None
    
    largestlet = None
    maxtimes = None
    for char in inputString:
        timeschar = checkForLet(char, inputString)
        if largestlet == None or maxtimes < timeschar:
            maxtimes = timeschar
            largestlet = char    
    
    #first smallest
    winner = None
    index = 0
    winning_in = None
    while index < len(inputString):
        let = inputString[index]
        if let > minLetter:
            if winner == None or let < winner:
                winner = let
                winning_in = index
        index += 1
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
            
    
    
