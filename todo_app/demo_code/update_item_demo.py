import requests
import dotenv
import os

dotenv.load_dotenv()

reqUrl = f"https://api.trello.com/1/cards/6633a8af3d54d9c028bfe33d"

query_params = {
    "key": os.getenv("TRELLO_API_KEY"),
    "token": os.getenv("TRELLO_API_TOKEN"),
    "idList": os.getenv("TRELLO_DONE_LIST_ID"),
}

response = requests.put(reqUrl,  params = query_params)

print(response.text)