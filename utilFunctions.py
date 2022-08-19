import api
from strategies import *

def setDictionary(game: dict) -> list:
    
    wordLen = game['word_length']
    # Pick the dictionary based on lenguage
    dictionary = api.getDictionary(game['language'])

    # Pick only the valid words from the dictionary (Equal length)
    utilDict = [i for i in dictionary if len(i) == wordLen]

    return utilDict

# Remove words from the dictionary according to API response, limiting the following words to send
def updateDict(dictionaries: list, word: str, answer: str) -> list:

    newUtilDictionary = []
    for dicNum, dic in enumerate(dictionaries):
        newDictionary = dic
        # Letters found with 2
        correctLetters = dict()
        # Letters found with 1
        detectedLetters = dict()

        for indx, l in enumerate(answer[dicNum]):
            # Found in correct position
            if l == '2':
                # Add letter to knowledge
                if word[indx] not in correctLetters:
                    correctLetters[word[indx]] = 1
                newDictionary = [i for i in newDictionary if i[indx] == word[indx]]
                # print(f'Keeping {word[indx]} in {indx}')
        for indx, l in enumerate(answer[dicNum]):
            if l == '1':
                if word[indx] not in detectedLetters:
                    detectedLetters[word[indx]] = 1
                else:
                    detectedLetters[word[indx]] += 1
                # The letter must be present in the word and not in the position
                # print(f'Deleting {word[indx]} in {indx}')
                newDictionary = [i for i in newDictionary if (word[indx] in i) and (word[indx] != i[indx])]

        for indx, l in enumerate(answer[dicNum]):
            if l == '0':
                # If letter is not present
                if word[indx] not in correctLetters and word[indx] not in detectedLetters:
                    # Remove words from the dictionary that contain the letter
                    newDictionary = [i for i in newDictionary if word[indx] not in i]
                    # print(f'Deleting {word[indx]} in {indx}')
                if word[indx] in correctLetters and word[indx] not in detectedLetters:
                    newDictionary = [i for i in newDictionary if word[indx] != i[indx]]

        newUtilDictionary.append(newDictionary) 
    return newUtilDictionary

# Strategy to select a word from the available pool
def selectWord(dictionaries: list, result: dict, fullDictionary: list, previousWord: str) -> str:

    d_sizes = []
    for d in dictionaries:
        d_sizes.append(len(d))
        
    # If the word is known and havent been sent yet
    if result:
        response = result['result']
        gameState = result['words_state']
        for indx, d in enumerate(d_sizes):
            if d == 1 and gameState[indx] is False:
                return dictionaries[indx][0]

    longest_dictionary_position = d_sizes.index(max(d_sizes))
    dictionary = dictionaries[longest_dictionary_position]
    

    # Strategy with low word count
    for d in dictionaries:
        if len(d) < 8 and len(d) > 3:
            dictionary = d
            # print(f'{dictionary[:10]}')
            word = lowCountStrategy(dictionary, fullDictionary, previousWord)
            if word != False:
                return word
    
    
    # print(f'Size: {len(dictionary)}')
    # print(f'{dictionary[:10]}')

    # Strategy of diferent letters with a large dictionary
    for w in dictionary:
        if len(set(w)) == len(w):
            word = w
            return word


    # If previous strategies didnt pick a word just pick the 1st available word, 
    # usually reserved for last one
    return dictionary[0]


def openingChoice(game: dict, dictionaries: list, result: dict, fullDictionary: list) -> str:
    if game['language'] == '/static/english.txt' and game['word_length'] == 5:
        return 'ORATE'
    
    if game['language'] == '/static/espanol.txt' and game['word_length'] == 5:
        return 'SALEN'
    
    else:
        return selectWord(dictionaries, result, fullDictionary, None)
