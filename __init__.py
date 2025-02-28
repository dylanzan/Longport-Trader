import os

from dotenv import load_dotenv

load_dotenv()

LONGPORT_API_APP_KEY=os.getenv("LONGPORT_API_APP_KEY")
LONGPORT_API_APP_SECRET=os.getenv("LONGPORT_API_APP_SECRET")
LONGPORT_API_ACCESS_TOKEN=os.getenv("LONGPORT_API_ACCESS_TOKEN")

_X_GROK_API_KEY = os.getenv('X_GROK_API_KEY')
_X_GROK_API_BASE_URL = os.getenv('X_GROK_API_BASE_URL')
_X_GROK_API_MODEL = os.getenv('X_GROK_API_MODEL')
