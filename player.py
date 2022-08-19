import api
import sys
from utilFunctions import *


def main():
  global r1
  # Set dictionary
  # gameNum = 6
  games = api.getGames()
  # print(games)
  totalTurns = 0
  totalGames = 0
  
  for game in games:
    fullDict = setDictionary(game)
    utilDicts = []
    gameNum = game['id']
    words_count = game['words_count']
    for _ in range(words_count):
      utilDicts.append(fullDict.copy())
  
    # Reset Debug
    api.reset(gameNum)
  
    turns = 0
    result = {}

    # First word 
    choosedWord = openingChoice(game, utilDicts, result, fullDict)
    result = api.play(gameNum, choosedWord)
    utilDicts = updateDict(utilDicts, choosedWord, result["result"])

    # Game Loop
    while True:
      turns += 1

      # Sending word to API
      choosedWord = selectWord(utilDicts, result, fullDict, choosedWord)
      # print(f'Sending: {choosedWord}')
      result = api.play(gameNum, choosedWord)

      # Update the available words according to the API response
      utilDicts = updateDict(utilDicts, choosedWord, result["result"])

      # Print for tracking
      # print(f'Response: {result["result"]}')
      # print(f'{result["words_state"]}')

      
      if result['finished']:
        totalGames += 1
        print(f'Finished. Word length: {game["word_length"]}, words number: {words_count}')
        print(f'Turns: {turns}\tLanguage: {game["language"]}\n================================================')
        # print(f'{turns}', end=' ')
        # sys.stdout.flush()
        totalTurns += turns
        break
    # Break for 1 game debug
    # break
  print(f'Total games: {totalGames}')
  print(f'Total turns: {totalTurns}')
  print(f'Turns per game app: {totalTurns/totalGames}')


if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    pass
  
