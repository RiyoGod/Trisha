from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME, COLLECTION_NAME

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

def save_conversation(user_id, message, response):
    """Save the conversation to MongoDB."""
    conversation = {"user_id": user_id, "message": message, "response": response}
    collection.insert_one(conversation)

def get_last_conversation(user_id):
    """Retrieve the last conversation for a user."""
    last_message = collection.find_one({"user_id": user_id}, sort=[("_id", -1)])
    return last_message["response"] if last_message else None
