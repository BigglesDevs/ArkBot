import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv

class MongoManager:
    def __init__(self):
        load_dotenv()
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db = self.client['arkbot_db']
        self.collection = self.db['channels']

    def set_channel(self, name, channel_id):
        self.collection.update_one(
            {"name": name},
            {"$set": {"channel_id": channel_id}},
            upsert=True
        )

    def get_channel(self, name):
        result = self.collection.find_one({"name": name})
        return result['channel_id'] if result else None
