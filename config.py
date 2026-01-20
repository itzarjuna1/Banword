import os
from os import getenv

# ------------------------------------------------

API_ID = int(os.environ.get("API_ID", "27795164"))
API_HASH = os.environ.get("API_HASH", "931051ff310e587ac41154ed3d516f06")

# ------------------------------------------------

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "snowy_x_handlerbot")

# -----------------------------------------------

OWNER_ID = int(os.environ.get("OWNER_ID", "7651303468"))
SPECIAL_ID = int(os.environ.get("SPECIAL_ID", "7651303468"))
# ------------------------------------------------

# ------------------------------------------------
LOGGER_ID = int(os.environ.get("LOGGER_ID", "-1003228624224"))
OTHER_LOGS = int(os.environ.get("OTHER_LOGS", "-1003228624224"))

# ------------------------------------------------

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://knight4563:knight4563@cluster0.a5br0se.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# ------------------------------------------------
