import re
from os import environ
from os import getenv

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# ----------------ʜᴇʀᴇ-ᴄᴏɴғɪɢ------------------#

API_ID = int(environ['27884171'])
API_HASH = environ['abe760b5d6b33e15c676577d6ae4a06a']
BOT_TOKEN = environ['7794116617:AAFa4twXPx8oxwVVkJFErldbrrYf8vOYet4']
OWNER_IDS = list(map(int, getenv("OWNER_IDS", "7759282826").split()))
PREMIUM_IDS = list(map(int, getenv("PREMIUM_IDS", "7759282826").split()))

# ----------------ᴄᴏɴғɪɢ-ᴇɴᴅ------------------#
