import api
from utilFunctions import *


if __name__ == '__main__':
  # Set dictionary
  gameNum = 5
  utilDict = setDictionary(gameNum)

  # Reset Debug
  api.reset(gameNum)
  input('Player Ready...')
  
  turns = 0
  # Game Loop
  while True:
    turns += 1

    # Sending word to API
    choosedWord = selectWord(utilDict)
    result = api.play(gameNum, choosedWord)

    # Print for tracking
    print(f'Sending: {choosedWord}')
    print(f'Response: {result["result"]}')

    # Update the available words according to the API response
    utilDict = updateDict(utilDict, choosedWord, result['result'][0])

    if result['finished']:
      print('Finished!')
      print(f'Turns taken: {turns}')
      break
