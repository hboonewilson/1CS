# CS 1210, Spring 2020, Discussion Section 3, Feb. 11, 2020

#
# TODAY'S WORK: The TA will demonstrate some of the parts in this file.
# Students will be graded on correct completion of Parts 5 and 6.
#
# PART 1. STUDENTS: Download three files from DS3 assignment on ICON:
# There should be
# - this file, ds3.py
# - wordsMany.txt, a set of 113,809 words permitted in crossword puzzles
#   from Moby Project (now at Project Gutenberg).
#        see http://icon.shef.ac.uk/Moby/mwords.html
#        and http://www.gutenberg.org/ebooks/3201
# - wordsFew.txt, a file containing three words
#
# PUT ALL THREE FILES IN THE SAME FOLDER
#
# PART 2. TA: demonstrate, explain the testWords function below.
# It is not necessary for students to understand how opening/reading files
# works right now.  Students only need to be able to use the function and
# modify the non-file-related part slightly.
#
# Run testWords on a couple examples:
#  1) with returnTrue(word) as the if condition,
#          testWords("wordsFew.txt") prints three words
#          NOTE: don't run with returnTrue(word) on wordsMany.txt.
#                You don't want to print 113,809 words!
#  2) with 'qi' in word
#     as the if condition, testWords('wordsMany.txt') prints eight words
#
def testWords(filename):
    fileStream = open(filename, 'r')
    for line in fileStream:
        word = line.strip()
        #if returnTrue(word):
        #if 'qi' in word:
        #if hasMoreThanTwentyChars(word):
        #if hasThreeConsecPairs(word):
        if hasFourConsecVowels(word):
            print(word)

# not a useful function except to understand basic structure of
# testWords above.
#
# Always returns True.
#
def returnTrue(string):
    return True

# PART 3. TA: finish this hasMoreThanTwentyChars(word) stub below
#
#     1) test it by calling it directly on a few words
#     2) test if more fully by calling it in testWords and
#                        calling testWords with wordsMany.txt
#        This should yield all words in wordsMany.txt longer than 20 chars.
#
#         Expected output:
#
#         >>> testWords("wordsMany.txt")
#         counterdemonstrations
#         hyperaggressivenesses
#         microminiaturizations
#
def hasMoreThanTwentyChars(word):
    return len(word) > 20

#
# PART 4. TA: describe and demonstrate solution to the following problem
#             posed on the well-known Car Talk radio show:
#
#        Problem: Find all words that contain three consecutive pairs of double letters.
#
#        Example: committee is *not* such as word.  There are three sets of double letters, but
#        there is an 'i' between the first ('mm') and second ('tt')
#
#        TA: After describing this code, execute testWords("wordsMany.txt") with
#            using if hasThreeConsecPairs(word):
#            instead of if returnTrue(word):
#            Four words should be printed out of the 113,809
#
#     Solution
#
def hasThreeConsecPairs(word):
    result = False
    index = 0
    while (index + 5) < len(word):
        if ((word[index] == word[index + 1]) and
            (word[index + 2] == word[index + 3]) and
            (word[index + 4] == word[index + 5])):
            result = True
            break
        index = index + 1
    return result

# PART5. Write function hasFourConsecVowels(word)
# that returns True if the given word contains four (or more) vowels in a row
# (consider only lowercase 'a', 'e', 'i', 'o', 'u' vowels, not 'y')
#
#
def checkVowel(word, index, origin):
    return (word[origin+index] == 'a' or word[origin+index] == 'e' or word[origin+index] == 'i' or word[origin+index] == 'o' or word[origin+index] == 'u')
# FOR YOUR TESTING:
# Test your code on the big wordsMany.txt file by using 
#         if hasFourConsecVowels(word):
# instead of other 'if's in testWords, and calling testWords("wordsMany.txt")

# You might be suprised to see how many English words have four consecutive vowels!

# change this to be correct
def hasFourConsecVowels(word):
    result = False
    x = 0
    while x + 3 < len(word):
        if checkVowel(word, 0, x) and checkVowel(word, 1, x) and checkVowel(word, 2, x) and checkVowel(word, 3, x):
            result = True
            break
        x += 1
    return result
#if ((word[x] == 'a' or word[x] == 'e' or word[x] == 'i' or word[x] == 'o' or word[x] == 'u')
# PART6. Complete function part6 so that it returns two things:
# 1) the largest character in inputString that is not a character in charsToIngore
# 2) the least index at which that character occurs.
# If there is no such character return None or both values
#
# The input will be a string of zero or more lower case characters.
# Use a simple loop. You may not use any string methods,
# but you may use the 'in' or 'not in' operators.
#
# E.g.
# >>> part6("bca", "")
# ('c', 1)
# >>> part6("agcdexfb", "ed")
# ('x', 5)
# >>> part6("agcdexfb", "edx")
# ('g', 1)
# >>> part6("baaaca", "abc")
# (None, None)
# >>> part6("baaaca", "bc")
# ('a', 1)
#
# Remember, as in HW1, to return two values, simply list both in the return
# statement with a comma separating them.
# E.g. return largestChar, indexOfLargestChar
#
def part6(inputString, charsToIgnore):
    largestChar = None
    indexOfLargestChar = None
    for i in range (0, len(inputString)):
        charinignore = False
        for char in charsToIgnore:
            if inputString[i] == char:
                charinignore = True
                break
        if not charinignore:
            if (largestChar == None) or (largestChar < inputString[i]):
                largestChar = inputString[i]
                indexOfLargestChar = i
    return largestChar, indexOfLargestChar





