from os import getenv


API_ID = int(getenv("API_ID", "23694600"))
API_HASH = getenv("API_HASH", "7bf5cc011eeab9270463dbb194689b51")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6879123652").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://sonudohare:chodubaksa@cluster0.bhh3z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "1002290479633"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "1002290479633"))


