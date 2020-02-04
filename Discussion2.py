# CS1210 Spring 2020, Discussion section 2, Feb. 4, 2020
#
# Complete each of the four functions and submit this file to your section
# DS2 assignment item in ICON.

# Q1. Given non-negative integer num, q1(num) should print one exactly one line:
# "num is not a multiple of 2, 7, or 14",
# "num is a multiple of 2" if num is a multiple of 2 but not 14,
# "num is a multiple of 7" if num is a multiple of 7 but not 14,
#  or "num is a multiple of 14" if num is a multiple of 14
# where where num in the output is the actual input number rather than the
# string 'num'

def q1 (num):
    if num % 14 == 0:
        print(f"{num} is a multiple of 14")
    elif num % 2 == 0:
        print(f"{num} is a multiple of 2")
    elif num % 7 == 0:
        print(f"{num} is a multiple of 7")
    else:
        print(f"{num} is not a multiple of 2, 7, or 14")
    

# Q2. Given non-negative integer n, q2(n) should call q1 for each integer from 1 up
# to and including n.  (Thus, if n is 0, it should not call q1 at all).
# q2 *must* use a WHILE loop to do the counting.
# Example output:
# >>> q2(3)
# 1 is not a multiple of 2, 7, or 14
# 2 is a mulitple of 2
# 3 is not a multiple of 2, 7, or 14

def q2(n):
    if n != 0:
        for i in range (1, n+1):
            q1(i)
        
# Q3.Complete function printDigitsOf
#
# Problem: How can we extract and print the digits of an integer using math?
#
# Some people might know that in Python we first convert the number to a
# string of digitas and then look at each character in the string. BUT, the goal
# here is to do it with just math - NO STRING OPERATIONS.
#
# HOW? Use this approach:
#
#    1.we can get last digit of an integer by using % 10 
#           digit = number % 10
#
#    2. we can get a new number with all but the last digit via
#           newNumber = number // 10
#    
#    3. we repeat those steps until nothing's left
#
#    USE A WHILE LOOP TO ACCOMPLISH THE ABOVE STEPS
#
#  HINT: First, yiou should try examples of 1 and 2 at a Python prompt to make
#  sure you understand. E.g. enter 432 % 10 and 432 // 10
#

def printDigitsOf(number):
    while number != 0:
        print(number % 10)
        number = (number // 10)

# Q4. Complete function sumDigitsOf
#
# Problem: create new function, sumDigitsOf(number),
# by slightly modifying printDigitsOf. Instead of printing the digits of the
# given number it should add up all the digits and return (*not* print) that
# sum

def sumDigitsOf(number):
    retsum = 0
    while number != 0:
        retsum += (number % 10)
        number = (number // 10)
    return retsum

    

