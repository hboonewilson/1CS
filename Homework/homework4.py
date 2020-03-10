def helperq1(letter, listInLists):
    count = 0
    for let in listInLists:
        if let == letter:
            count += 1
def q1(listOfLists, infoDict):
    retlis = []
    for lis in listOfLists:
        blue = 0
        green = 0
        red = 0 
        for el in lis:
            if el in infoDict:
                if infoDict[el] == 'red':
                    red += 1
                elif infoDict[el] == 'blue':
                    blue += 1
                else:
                    green += 1
            else:
                green += 1
        if blue > green and blue > red:
            small = None
            for dex in lis:
                if small ==  None or small > dex:
                    small = dex
            retlis += [small]
        elif red > green and red > blue:
            large = None
            for dex in lis:
                if large == None or large < dex:
                    large = dex
            retlis += [large]
        else:
            most = None
            count = 0
            for dex in lis:
                times = lis.count(dex)
                if most == None:
                    most = dex
                    count = times
                else:
                    if times > count:
                        most = dex
                        count = times 
                    elif times == count:
                        if dex < most:
                            most = dex
                        else:
                            pass
            retlis.append(most)
    return retlis

def analyzeTexts(filename, minWordLengthToConsider = 1):
    readfile = open(filename, 'r', encoding='utf-8')
    ham = 0
    spam = 0
    totalwordsham = 0
    totalwordsspam = 0
    hamspam ={'ham':{}, 'spam': {}}
    for line in readfile:
        linelis = line.split()
        if linelis[0] == 'ham':
            for i in range(1, len(linelis)):
                word = linelis[i].strip(".?:;',!@#()$%^&*-_+={}[]|\<>")
                word = word.lower()
                if word in hamspam['ham'] and len(word) > minWordLengthToConsider:
                    hamspam['ham'][word] += 1
                elif word not in hamspam['ham'] and len(word) > minWordLengthToConsider:
                    hamspam['ham'][word] = 1
                totalwordsham += 1
            ham += 1
        else:
            for i in range(1, len(linelis)):
                word = linelis[i].strip(".?:;',!@#()$%^&*-_+={}[]|\<>")
                word = word.lower()
                if word in hamspam['spam'] and len(word) > minWordLengthToConsider:
                    hamspam['spam'][word] += 1
                elif word not in hamspam['spam'] and len(word) > minWordLengthToConsider:
                    hamspam['spam'][word] = 1
                totalwordsspam += 1
            spam += 1
    hamtups = []    
    for word in hamspam['ham']:
        hamtups.append((word, hamspam['ham'][word]))
    spamtups = []    
    for word in hamspam['spam']:
        spamtups.append((word, hamspam['spam'][word]))
    hamtups = sorted(hamtups, key = lambda item: item[1], reverse=True)
    spamtups = sorted(spamtups, key = lambda item: item[1], reverse=True)
    print(f'Number of Ham messages: {ham}')
    print(f"Number of Spam messages: {spam}")
    print()
    print(f"Total words in Ham: {totalwordsham}")
    print(f"Total words in Spam: {totalwordsspam}")
    print()
    print("12 Most common words in Ham:")
    for i in range(0, 12≠±):
        frequency = hamtups[i][1] / totalwordsham
        frequency = round(frequency, 2)
        print(f"{i+1}. Word: '{hamtups[i][0]}' Count: {hamtups[i][1]} Frequency:{frequency}%")
    print()
    print('12 Most common words in Spam:')
    for i in range(0, 12):
        frequency = (spamtups[i][1] / totalwordsspam)
        frequency = round(frequency, 2)
        print(f"{i+1}. Word: '{spamtups[i][0]}' Count: {spamtups[i][1]} Frequency:{frequency}%")
              
    

    
        
    