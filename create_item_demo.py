import requests

reqUrl = "https://api.trello.com/1/cards"

query_params = {
    "key":"ff02dc85cb92b92ec769718e2a6befa6",
    "token":"ff02dc85cb92b92ec769718e2a6befa6",
    "idlist":"6630eca0d794a3515318f326",
    "name":"Python Created Todo"
}

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
}

payload = ""

response = requests.post(reqUrl, data=payload,  headers=headersList, params = query_params)

print(response.text)