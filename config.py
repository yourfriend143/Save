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
Credit = getenv("Credit","Gumnaam")
c_url = getenv("c_url","https://t.me/Bhardwaj1434")
API_ID = int(getenv("API_ID", "23283708"))
API_HASH = getenv("API_HASH", "7805011fb84729023531f0fa3f000bec")
BOT_TOKEN = getenv("BOT_TOKEN", "8579722162:AAHej40kAnYfJ2r_bzOZkWokZCUovpuMxeE")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6481888008").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://rj5706603:O95nvJYxapyDHfkw@cluster0.fzmckei.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002170739108"))
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002534290926"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "10000"))
WEBSITE_URL = getenv("WEBSITE_URL", "seturl")
AD_API = getenv("AD_API", "bd3e6eda2cae3645c953ce93c38725bc3c5ebc93")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
