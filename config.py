# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""
img_url = getenv("img_url","https://envs.sh/24T.jpg")
Credit = getenv("Credit","@NOTHING_SAINI19 𝙎𝘼𝙄𝙉𝙄 𝙎𝘼𝙃𝘼𝘽")
c_url = getenv("c_url","https://t.me/nothing_saini19")
API_ID = int(getenv("API_ID", "24861505"))
API_HASH = getenv("API_HASH", "fad28c88a18f4f2d9c67c2c08c19696f")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7944235618").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "-1002977757679")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002913007404"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "10000"))
WEBSITE_URL = getenv("WEBSITE_URL", "seturl")
AD_API = getenv("AD_API", "bd3e6eda2cae3645c953ce93c38725bc3c5ebc93")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
