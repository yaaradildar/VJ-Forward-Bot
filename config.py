# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "16253557"))
    API_HASH = environ.get("API_HASH", "81171c25e4cb9062cb10da8b7730432a")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "vjbot") 
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://MRDAXX:MRDAXX@mrdaxx.prky3aj.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "vj-forward-bot")
    BOT_OWNER = int(environ.get("BOT_OWNER", "1996039956"))

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
