import os
from dotenv import load_dotenv

class ConfigManager:
    def __init__(self):
        load_dotenv()
        self.DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
        self.RCON_HOST = os.getenv("RCON_HOST")
        self.RCON_PORT = int(os.getenv("RCON_PORT"))
        self.RCON_PASSWORD = os.getenv("RCON_PASSWORD")
        self.MONGO_URI = os.getenv("MONGO_URI")
