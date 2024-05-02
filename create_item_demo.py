import requests
import dotenv
import os

dotenv.load_dotenv()


reqUrl = "https://api.trello.com/1/cards"

query_params = {
    "key": os.getenv("TRELLO_API_KEY"),
    "token": os.getenv("TRELLO_API_TOKEN"),
    "idList": "6630eca10b5e88d30c557a24",
    "name" : "Python Created Todo 2"
}

response = requests.post(reqUrl,  params = query_params)

print(response.text)