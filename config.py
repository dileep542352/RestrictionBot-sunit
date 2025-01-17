from os import getenv


API_ID = int(getenv("API_ID", "27256080"))
API_HASH = getenv("API_HASH", "0603cf221dfc7bea62656d11a57f9e41")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5565741405 6107581019 8001147497").split()))
MONGO_DB = getenv("MONGO_DB", "")

CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", ""))


