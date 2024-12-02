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

API_ID = environ['24740695']
API_HASH = environ['a95990848f2b93b8131a4a7491d97092']
BOT_TOKEN = environ['7821314898:AAHgRpDfbpfsqefrGUUYKlOtigbqNSc4gA0']
OWNER_IDS = list(map(int, getenv("OWNER_IDS", "7877197608").split()))
PREMIUM_IDS = list(map(int, getenv("PREMIUM_IDS", "7877197608").split()))

# ----------------ᴄᴏɴғɪɢ-ᴇɴᴅ------------------#
