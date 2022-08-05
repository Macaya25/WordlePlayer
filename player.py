import api
from utilFunctions import *


if __name__ == '__main__':
  # Set dictionary
  gameNum = 5
  fullDict = setDictionary(gameNum)
  utilDict = fullDict.copy()

  # Reset Debug
  api.reset(gameNum)
  
  turns = 0
  # Game Loop
  while True:
    turns += 1
    i = input('Send: ').upper()
    if i in utilDict:
      result = api.play(gameNum, i)
      print(result)
      utilDict = updateDict(utilDict, i, result['result'][0])
      print(utilDict)
    else:
      print('Invalid word.')
      continue
    if result['finished']:
      print('Finished!')
      print(f'Turns taken: {turns}')
      break
