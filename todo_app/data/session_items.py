import requests, os, datetime, dotenv
 
class List:  
    def __init__(self, id, name):  
        self.id = id  
        self.name = name

class Card:

    def __init__(self, id, name, idList, desc, due):
        self.id = id
        self.name = name
        self.idList = idList
        self.desc = desc
        try:
            self.due = self.due = datetime.strptime(due,'%Y-%m-%dT%H:%M:%S.%fZ')
        except:
            self.due = None

def getAuth():
    #Retrieves Authorization
    
    auth = []
    auth.append(os.getenv('TRELLO_KEY'))
    auth.append(os.getenv('TRELLO_TOKEN'))

        
    return auth

def getBoardId():
    #Retrieves Board ID
    boardID = os.getenv('BOARD_ID')
    return boardID

def getLists():
    #GETS ALL lists by board ID
    auth = getAuth()
    boardID = getBoardId()
    lists = []

    for list in(requests.get(f'https://api.trello.com/1/boards/{boardID}/lists?key={auth[0]}&token={auth[1]}')).json():
        lists.append(List(list['id'],list['name']))
    return lists

def getCards():
    #GETS ALL cards by board ID
    auth  = getAuth()
    boardID = getBoardId()
    
    cards = []
    for card in (requests.get(f'https://api.trello.com/1/boards/{boardID}/cards?key={auth[0]}&token={auth[1]}')).json():
        cards.append(Card(card['id'],card['name'],card['idList'],card['desc'],card['due']))
    return cards

def moveCard(card_id, listID):
    #MOVEs card by list ID
    auth = getAuth()
    move= requests.put(f'https://api.trello.com/1/cards/{card_id}?key={auth[0]}&token={auth[1]}&idList={listID}').json()

    return move

def addCard(name, listId):
    #ADDs card by list ID
    auth = getAuth()
    add= requests.post(f'https://api.trello.com/1/cards/?key={auth[0]}&token={auth[1]}&idList={listId}&name={name}').json()
    return add

def removeCard(card_id):
    #DELETEs card by card ID 
    auth = getAuth()
    delete= requests.put(f'https://api.trello.com/1/cards/{card_id}?key={auth[0]}&token={auth[1]}').json()
    return delete