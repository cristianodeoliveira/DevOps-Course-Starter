import requests
import dotenv
import os

dotenv.load_dotenv()


reqUrl = "https://api.trello.com/1/cards"

query_params = {
    "key": os.getenv("TRELLO_API_KEY"),
    "token": os.getenv("TRELLO_API_TOKEN"),
    "idList": os.getenv("TRELLO_TODO_LIST_ID"),
    "name" : "Python Created Todo 3"
}

response = requests.post(reqUrl,  params = query_params)

print(response.text)