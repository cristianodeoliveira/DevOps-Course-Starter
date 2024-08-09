import pymongo
import dotenv
import os

dotenv.load_dotenv()

client = pymongo.MongoClient (os.getenv("MONGODB_CONNECTION_STRING"))

db = client[os.getenv("MONGODB_DB_NAME")]
collection = db[os.getenv("MONGODB_COLLECTION_NAME")]

# insert a record
#collection.insert_one ({"description":"First pymongo document"})
#collection.insert_one ({"description":"A second pymongo document"})
#collection.insert_one ({"description":"An updatable entry","type":"updatable"})

#update an entry
#collection.update_one({"type":"updatable"},{"$set":{"description":"CHANGED!!!"}})

# read all records
list(collection.find())

#print (client.list_database_names())
print (collection)