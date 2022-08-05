import api
import pandas as pd

def setDictionary(gameNum):
  games = api.getGames()
  # Pick the desired game from api
  for g in games:
    if g['id'] == gameNum:
      game = g
  wordLen = game['word_length']
  # Pick the dictionary based on lenguage
  dictionary = api.getDictionary(game['language'])
  df = pd.DataFrame(dictionary)

  # Pick only the valid words from the dictionary
  utilDict = df[(df[0].map(len) == wordLen)]
  utilDict = utilDict[0].to_list()

  return utilDict

def updateDict(dictionary, word, answer):
    newDictionary = dictionary

    # Letters found with 2
    correctLetters = dict()
    # Letters found with 1
    detectedLetters = dict()

    for indx, l in enumerate(answer):
        # Found in correct position
        if l == '2':
            # Add letter to knowledge
            if word[indx] not in correctLetters:
                correctLetters[word[indx]] = 1
            newDictionary = [i for i in newDictionary if i[indx] == word[indx]]
        # TODO
        elif l == '1':
            if word[indx] not in detectedLetters:
                detectedLetters[word[indx]] = 1
            else:
                detectedLetters[word[indx]] += 1
            # The letter must be present in the word and not in the position
            newDictionary = [i for i in newDictionary if (word[indx] in i) and (word[indx] != i[indx])]
        elif l == '0':
            # If letter is not present
            if word[indx] not in correctLetters:
                # Remove words from the dictionary that contain the letter
                newDictionary = [i for i in newDictionary if word[indx] not in i]
    return newDictionary
