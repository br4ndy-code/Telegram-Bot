import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
I18N_DOMAIN = 'BroCat'
BASE_DIR = Path(__file__).parent
LOCALES_DIR = BASE_DIR / 'locales'
