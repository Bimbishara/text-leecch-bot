import os

API_ID    = os.environ.get("API_ID", "20891424")
API_HASH  = os.environ.get("API_HASH", "f29cef7feff53b2d9321c6b9e5d69b21")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7008305807:AAHHCLHfQqP7Fo0Sv78JR6ghBEiIybCc7TU") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
