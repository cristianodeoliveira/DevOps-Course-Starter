import os
from dotenv import load_dotenv, find_dotenv
import pytest
import pymongo
from todo_app import app
import mongomock

@pytest.fixture

def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    
    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client
        
def test_index_page(client):
    # Arrange
    
    mongo_client = pymongo.MongoClient (os.getenv("MONGODB_CONNECTION_STRING"))
    db = mongo_client[os.getenv("MONGODB_DB_NAME")]
    collection = db[os.getenv("MONGODB_COLLECTION_NAME")]
        
    test_document = {
        "name": "Test Item",
        "status": "To Do"
    }
    
    collection.insert_one(test_document)    
    
    #Act
    response = client.get('/')
    
    # Assert
    assert response.status_code == 200
    assert 'Test Item' in response.data.decode()
