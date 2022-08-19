import requests

api_url = 'https://pds-wordie.herokuapp.com'
player_key = 'OSUJGUL'

# Obtener juegos activos
def getGames() -> list:
    response = requests.get(f'{api_url}/api/games/')
    games = response.json()['games']
    return games

# Obtener diccionario
def getDictionary(language) -> list:
    file_url = f'{api_url}{language}'
    r = requests.get(file_url)

    requests.enconding = 'cp1252'
    text = r.content.decode('cp1252', errors='ignore')

    text_list = text.split('\n')
    words = [w.strip().upper() for w in text_list]

    return words

# Enviar una jugada
def play(game, word) -> requests.Response:
    data = {
        'game': game,
        'key': player_key,
        'word': word
    }
    r = requests.post(f'{api_url}/api/play/', data=data)
    return r.json()

# Resetear un juego para volver a empezar (se eliminan las jugadas previas)
def reset(game: int) -> requests.Response:
    data = {
        'game': game,
        'key': player_key
    }
    r = requests.post(f'{api_url}/api/reset/', data=data)
    return r.json()
