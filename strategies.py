
def lowCountStrategy(dictionary, fullDictionary, previousWord):
    # Find index of different letters between words in available dictionary
    for ind, c in enumerate(dictionary[0]):
        if c != dictionary[1][ind]:
            indx = ind
            break
    letters = set([i[indx] for i in dictionary])
    # print(f'\tLetters: {letters}')

    # Search words in full dictionary that have a decent number of "problem letters" 
    # to delete them from the available dictionary
    orderedWords = findWordsBasedOnLetters(letters, fullDictionary)
    if orderedWords:
        if previousWord in orderedWords:
            pos = orderedWords.index(previousWord)
            if len(orderedWords) > pos + 1:
                return orderedWords[pos + 1]
            else:
                return False
        return orderedWords[0]
    return False


def findWordsBasedOnLetters(letters: list, fullDictionary: dict):
    tempWords = []
    for fullWord in fullDictionary:
        if list(c in letters for c in fullWord).count(True) > 1:
            tempWords.append(fullWord)
    # print(f'Temp: {tempWords}')
    
    # Order the available words from more useful to less (Amount of times it appears)
    orderedWords = []
    if tempWords:
        n = 0
        for w in tempWords:
            t = list(c in letters for c in w).count(True)
            if t > n and len(set(w)) == len(w):
                n = t
                orderedWords.append(w)
            else:
                orderedWords.insert(0, w)
    return orderedWords