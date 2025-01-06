from os import getenv


API_ID = int(getenv("API_ID", "20483216"))
API_HASH = getenv("API_HASH", "2518170d3dd939b3f2893cb0aae805c4")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5565741405 6107581019").split()))
MONGO_DB = getenv("MONGO_DB", "")

CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", ""))


