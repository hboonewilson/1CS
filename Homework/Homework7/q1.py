'''
Implement function egypt(numerator, denominator) that uses the greedy strategy presented in slides 7 and 8 of Lecture 30 (April 13) to determine a set of distinct (i.e. all different) Egyptian fractions that sum to numerator/denominator. You may assume numerator and denominator are positive integers and that numerator is less than or equal to denominator. Your function should both 1) print a readable "equation" showing the result (see examples below) and 2) return a list of Egyptian fraction denominators
'''
def egypt(num, den):
    denEval = 2
    fracList = []
    numWh = num
    denWh = den
    notDone = True
    while notDone:
        if (numWh * denEval) > denWh:
            fracList.append(denEval)
            numWh = numWh * denEval - denWh
            denWh = denWh * denEval            
        elif numWh * denEval == denWh:
            notDone = False
            fracList.append(denEval)            
            pState = f'{num}/{den} = '
            for frac in fracList:
                frac = str(frac)
                fraction = '1/' + frac + ' + '
                pState += fraction
            print(pState[:-2])
            return fracList 
        denEval += 1
        