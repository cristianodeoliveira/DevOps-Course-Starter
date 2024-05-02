import requests
import os

def add_item(title):
    reqUrl = "https://api.trello.com/1/cards"

    query_params = {
        "key": os.getenv("TRELLO_API_KEY"),
        "token": os.getenv("TRELLO_API_TOKEN"),
        "idList": os.getenv("TRELLO_TODO_LIST_ID"),
        "name" : title
    }

    response = requests.post(reqUrl,  params = query_params)

    print(response.text)