def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)
        
def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

def printList(inList):
    #each time print input list is and the current input list
    print("input is: ", inList)
    #if the input list is empty return nothing and end function
    if inList == []:
        return
    #if input list isn't empty print the input list and what it'sremoving
    else:
        print(inList[0])
        #recall the printList function
        printList(inList[1:])

def printListReverse(inList):
    if inList == []:
        return
    else:
        print(inList[-1])
        printListReverse(inList[:-1])

def printListReverse2(inList):
    print("entering printListReverse with input: ", inList)
    if inList == []:
        return
    else:
        printListReverse2(inList[1:])
        print(inList[0])
    print("leaving printListReverse")

def reverseString(inString):
    if inString == '':
        return ''
    elif len(inString) == 1:
        return inString
    else:
        return(reverseString(inString[1:]) + inString[0])

def BlastOff(n):
    if n<1:
        print("Blast off")
    else:
        print(n)
        BlastOff(n-1)
