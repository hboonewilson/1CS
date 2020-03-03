# CS 1210, Spring 2020
# Discussion section 5, March 3

# DISCUSSION SECTION WORK:
#

# 1. Have students download this file, ds5.py, and birdsseen.txt from ICON link
#
# 2. (5 MINUTES) EVERYONE.  Try these things in Python interpreter:
#     >>> dict1 = {1: 2, "frog": 4, 3: "hi"}
#     >>> len(dict1)              should yield 3 (number of key-value pairs)
#     >>> dict1[1]                 should yield 2
#     >>> dict1[3]                 should yield "hi"
#     >>> dict1["frog"]          should yield 4
#     >>> dict1[2]                 should yield error
#     >>> 2 in dict1              should yield False                                         in the dictionary.
#     >>> dict2 = {}
#     >>> len(dict2)              should return 0
#
#     Finally, you can iterate over keys (though you don't know the order in which
#     you'll get them:
#
#     >>> for key in dict1:
#                  print(key, dict1[key]))
#
#     yields (something like):
#       1 2
#       frog 4
#       3 hi
#
# 3. (10 MINUTES)
#
#     TA: explain makeBirdDict. Input file contains list of birds someone
#     someone has seen over time (so the same kind of bird can appear multiple
#     times in the file.  birsseen.txt is a sample input file.
#
#     Demo: birdDict = makeBirdDict("birdsseen.txt")
#
#     Now suppose we have a bird sightings dictionary.  How can we extract the
#     most seen bird?
#     TA: explain how mostSeenBird() function works.  
#     Demo: mostSeenBird(birdDict)
#
# 4. STUDENTS:  Complete function part4 as specified below.
# 
# 5. STUDENTS: review printLetterCounts, which was discussed at the end
#      of March 2 lecture and provided for study
#    Then complete   printLetterCounts2, which is the same as printLetterCounts
#    except must use dictionaries instead of lists.
#
#  6. SUBMIT THIS FILE, in which nothing should be changed except part4 and
#     printLetterCounts2
#

#####

# FOR PART 3 (LED BY TA)
# return a dictionary in which the keys are bird types and the associated values are
# the numbers of times that bird type appears in the input file.
#
def makeBirdDict(fileName):
    birdDict = {}
    inFile = open(fileName, 'r')

    # for each bird type read from file, if already in dictionary,
    # increment the associated count, otherwise add it to
    # dictionary with count of 1.
    for line in inFile:
        birdType = line.strip()
        if birdType in birdDict:
            birdDict[birdType] = birdDict[birdType] + 1
        else:
            birdDict[birdType] = 1
    inFile.close()
    return(birdDict)

# Given a dictionary of the form returned by makeBirdDict, print
# information about the most seen bird, i.e. the bird type with highest associated value
#
def mostSeenBird(birdDict):
    mostSeenBird = None
    mostSeenCount = None
    for key in birdDict:
        if (mostSeenCount == None) or (birdDict[key] > mostSeenCount):
            mostSeenBird = key
            mostSeenCount = birdDict[key]
    print("The most seen bird was '{}', sighted {:d} times.".format(mostSeenBird, mostSeenCount))

# FOR PART 4
#
# Conmplete function part4(listOfStrings) that takes a list of strings as input
# and returns a dictionary where integer key k is in the dictionary and has 
# value v exactly when there are v length-k strings in the input list.
# For example,
# >>> part4(["a", "b", "cc", "zqsrtsssss", " ", "Z12", "!$"])
# {1: 3, 2: 2, 10: 1, 3: 1}
#
def part4(listOfStrings):
    result = {}
    for item in listOfStrings:
        if len(item) in result:
            result[len(item)] += 1
        else:
            result[len(item)] = 1
    return result

# FOR PART 5
#
# printLettersCounts prints the number of occurrences in inputString
# of each letter in letters.
# For example, printLetterCounts("This is a sentence containing a variety of letters", "aeiouy")
# yields:
#
#  'This is a sentence containing a variety of letters' has:
#       4 'a's
#       6 'e's
#       5 'i's
#       2 'o's
#       0 'u's
#       1 'y's
#       and 32 other characters
#
def printLetterCounts(inputString, letters):

    # 1. create a list, letterCounts, containing a 0 for each letter in letters
    letterCounts = len(letters) * [0]
    
    # 2. go through characters of string incrementing appropriate letterCounts item if char in letters - l
    for char in inputString:
        if char in letters:
            charPositionInLetters = letters.index(char)
            letterCounts[charPositionInLetters] = letterCounts[charPositionInLetters] + 1
    
    # at this point, values in letterCounts should contain correct counts of
    #     of number of times chars in letters appear in inpuString
    #     E.g. for printLetterCounts('this is a sentence', 'aze')
    #             letterCounts should be [1, 0, 3]
    # 3. compute (and store as otherChars Count) number of characters in inputString *not* in letters 
    otherCharsCount = len(inputString) - sum(letterCounts)
    
    # 4. print results
    print("'{}' has:".format(inputString))
    for l in letters:
        print("\t{} '{}'s".format(letterCounts[letters.index(l)], l))
    print("\tand {} other characters".format(otherCharsCount))

# NOTE: this code will crash if you run it before completing Step 1.
#       After completing step 1, you can test it and it will at least not crash.
#
def printLetterCounts2(inputString, letters):

    # 1. create an empty dictionary. Use variable name letterCounts
    # 
    letterCounts = {}
    
    # 2. go through characters of string. If an entry for that characters
    #     already appears in dictionary, increment it. Otherwise, add an entry
    #     with value 1.  (Note: this is *just* like the code in makeBirdDict!)
    for char in inputString:
        if char in letters:
            if char in letterCounts:
                letterCounts[char] += 1
            else:
                letterCounts[char] = 1
               
    # uncomment the next line if you want to see the dictionary:
    print(letterCounts)
    
    # 3. compute (and store as otherChars Count) number of characters in inputString *not* in letters 
    # NOTE: sum(letterCounts.values()) adds together all the values associated with all the keys in
    # the dictionary.  Since we haven't mentioned the sum function in class, WE'VE DONE THIS LINE
    # FOR YOU - DON'T CHANGE IT.
    otherCharsCount = len(inputString) - sum(letterCounts.values())
    
    # 4. print results
    #
    # YOU JUST NEED TO CHANGE ONE LINE HERE - the one with "... something ...".
    #
    # There is a small difficulty to deal with here.  If any letter of letters is not
    # in inputString, that letter will have no dictionary entry. So you need to handle
    # this special 0-occurrence case.  You can either explicitly check
    # via, e.g., 'if l in letterCounts:' or just use letterCounts.get(l,0).
    # The second argument to the 'get' method is the value to return if the first argument
    # is *not* in the dictonary!
    #
    print("'{}' has:".format(inputString))
    for l in letters:
        if l in letterCounts:
            print(f"\t{letterCounts[l]} '{l}'s")
        else:
            print(f"\t0 '{l}'s")
    print("\tand {} other characters".format(otherCharsCount))
