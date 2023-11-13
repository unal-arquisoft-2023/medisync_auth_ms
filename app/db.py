
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(dotenv_path=Path('.env'))
MONGO_URI = os.getenv("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(MONGO_URI)
    
auth_db = client["archisoft"]["auth"]
permissions_db = client["archisoft"]["permissions"]
roles_db = client["archisoft"]["roles"]

fake_users_db = {
    "johndoe": {
        "id" : "1",
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
    },
    "alice": {
        "id" : "2",
        "username": "alice",
        "full_name": "Alice Chains",
        "email": "alicechains@example.com",
    },
}

fake_auth_db = {
    "1": {
        "id" : "1",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "role": "admin",
        "user_id": "1"
    },
    "2": {
        "id" : "2",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "role": "patient",
        "user_id": "2"
    }
}

fake_permissions_db = {
    "/appointments": {
        "admin": ["GET", "POST", "PUT", "DELETE"],
        "patient": ["GET"],
    }
}


