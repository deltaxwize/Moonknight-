import os
import json
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

# Load environment variables from config.env
load_dotenv("config.env")

# Logging
LOG_FILE_NAME = os.getenv("LOG_FILE_NAME", "bot.log")

# Bot Configuration
PORT = int(os.getenv("PORT", 5010))
OWNER_ID = int(os.getenv("OWNER_ID", 0))

MSG_EFFECT = int(os.getenv("MSG_EFFECT", 0))

# Shortener
SHORT_URL = os.getenv("SHORT_URL", "")
SHORT_API = os.getenv("SHORT_API", "")
SHORT_TUT = os.getenv("SHORT_TUT", "")

SESSION = os.getenv("SESSION", "")
TOKEN = os.getenv("TOKEN", "")
API_ID = os.getenv("API_ID", "")
API_HASH = os.getenv("API_HASH", "")
WORKERS = int(os.getenv("WORKERS", 5))

# Database
DB_URI = os.getenv("DB_URI", "")
DB_NAME = os.getenv("DB_NAME", "")

# Force Subscription Channels (stored as JSON string in .env)
FSUBS = json.loads(os.getenv("FSUBS", "[]"))

# Database Channel
DB_CHANNEL = os.getenv("DB_CHANNEL", "")

# Auto Delete Timer
AUTO_DEL = int(os.getenv("AUTO_DEL", 300))

# Admin IDs (stored as JSON string in .env)
ADMINS = json.loads(os.getenv("ADMINS", "[]"))

# Bot Settings
DISABLE_BTN = os.getenv("DISABLE_BTN", "false").lower() == "true"
PROTECT = os.getenv("PROTECT", "false").lower() == "true"

# Messages Configuration
MESSAGES = {
    "START": os.getenv("START", ""),
    "FSUB": os.getenv("FSUB", ""),
    "ABOUT": os.getenv("ABOUT", ""),
    "REPLY": os.getenv("REPLY", ""),
    "SHORT_MSG": os.getenv("SHORT_MSG", ""),
    "START_PHOTO": os.getenv("START_PHOTO", ""),
    "FSUB_PHOTO": os.getenv("FSUB_PHOTO", ""),
    "SHORT_PIC": os.getenv("SHORT_PIC", ""),
    "SHORT": os.getenv("SHORT", ""),
}

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger
