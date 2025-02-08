import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY" , "AIzaSyA7Fge2TBe8XlQindNtSxPg98u5oV-DHBE")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")

DATABASE_NAME = "TrishaDB"
COLLECTION_NAME = "Conversations"
