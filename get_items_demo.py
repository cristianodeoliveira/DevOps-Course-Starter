import requests
import dotenv
import os

dotenv.load_dotenv()

board_id = os.getenv("TRELLO_BOARD_ID")

reqUrl = f"https://api.trello.com/1/boards/{board_id}/lists"

query_params = {
    "key": os.getenv("TRELLO_API_KEY"),
    "token": os.getenv("TRELLO_API_TOKEN"),
    "cards" : "open"
}

response = requests.get(reqUrl, params = query_params)

response_list = response.json()

for trello_list in response_list:
    for trello_card in trello_list['cards']:
        print(trello_card['name'])

print(response.status_code)