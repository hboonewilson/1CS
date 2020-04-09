def helperq1(letter, listInLists):
    count = 0
    for let in listInLists:
        if let == letter:
            count += 1
def q1(listOfLists, infoDict):
    retlis = []
    for lis in listOfLists:
        if lis == []:
            retlis.append(None)
        else:
            blue = 0
            green = 0
            red = 0
            most = None
            most_count = 0
            big = max(lis)
            little = min(lis)
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
                look = lis.count(el)
            if most == None or most_count < look:
                most = el
                most_count = look
            elif most_count == look:
                if most > el:
                    most = el
            if blue > green and blue > red:
                retlis.append(little)
            elif red > green and red > blue:
                retlis.append(big)
            else:
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
                word = linelis[i].strip(".?:;',!@#()$%^&*/-_+={}[]|\<>")
                word = word.lower()
                if word in hamspam['ham'] and len(word) > minWordLengthToConsider:
                    hamspam['ham'][word] += 1
                elif word not in hamspam['ham'] and len(word) > minWordLengthToConsider:
                    hamspam['ham'][word] = 1
                totalwordsham += 1
            ham += 1
        else:
            for i in range(1, len(linelis)):
                word = linelis[i].strip('.?:;",!@#()$%^&*/-_+={}[]|\<>')
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
    
    print()
    print(f'Number of Ham messages: {ham}')
    print(f"Number of Spam messages: {spam}")
    print()
    print(f"Total words in Ham: {totalwordsham}")
    print(f"Total words in Spam: {totalwordsspam}")

    print()

    print("12 Most common words in Ham:")
    for i in range(0, 12):
        frequency = hamtups[i][1] / totalwordsham
        frequency = round(frequency, 2)
        print(f"{i+1}. Word: '{hamtups[i][0]}' Count: {hamtups[i][1]} Frequency:{frequency}%")

    print()

    print('12 Most common words in Spam:')
    for i in range(0, 12):
        frequency = (spamtups[i][1] / totalwordsspam)
        frequency = round(frequency, 2)
        print(f"{i+1}. Word: '{spamtups[i][0]}' Count: {spamtups[i][1]} Frequency:{frequency}%")
