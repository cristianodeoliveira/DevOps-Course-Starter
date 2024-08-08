import pymongo
import os

from todo_app.data.item import Item

client = pymongo.MongoClient (os.getenv("MONGODB_CONNECTION_STRING"))

db = client[os.getenv("MONGODB_DB_NAME")]
collection = db[os.getenv("MONGODB_COLLECTION_NAME")]


def add_item(new_todo_title: str):
    new_item = {
        "name":new_todo_title,
        "status":"To Do"
    }
    collection.insert_one(new_item)

def get_items():
    mongodb_documents = list(collection.find())
    
    items = []
    for document in mongodb_documents:
        item = Item.from_mongo_document(document)
        items.append(item)
    
    return items
        

def move_item_to_done():
    pass