from os import getenv


API_ID = int(getenv("API_ID", "23694600"))
API_HASH = getenv("API_HASH", "7bf5cc011eeab9270463dbb194689b51")
BOT_TOKEN = getenv("BOT_TOKEN", "")
AUTH = list(map(int, getenv("AUTH", "6879123652").split()))
SESSION = getenv("SESSION", "")

FORCESUB = int(getenv("FORCESUB", ""))
