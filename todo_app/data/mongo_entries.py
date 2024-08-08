import pymongo
import os

client = pymongo.MongoClient (os.getenv("MONGODB_CONNECTION_STRING"))

db = client[os.getenv("MONGODB_DB_NAME")]
collection = db[os.getenv("MONGODB_COLLECTION_NAME")]


def add_item(new_todo_title: str):
    new_item = {
        "name":new_todo_item,
        "status":"To Do"
    }
    collection.insert_one(new_item)

def get_item():
    pass

def move_item_to_done():
    pass