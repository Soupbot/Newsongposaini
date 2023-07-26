import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCO5p9kWJ8G5ju4XLWE_eMQQEEBXYcNKaOiJBVR6zL1KjAI1qZM7Pj01_qjldNCJWMvSRStqibhVC_wcTGviELKpfsYCvp8BE4rMOKF8l40ACvLzXSCLko_fkvJsr2_mr0mD_2M0uweFeEhNZGAxHooIOgb-cYmRxwDtoB34M92xDZGOS8mZJSXoKZolhhbVWgXXcQeUlliLYgg8B7GLYueO0-ynT32P_pY47I3V3fIH-6oTzHqQr9PGZ3XQRA1Q7mpHh4-ZPxLAofCFU6mB8CH-dYrYRX7obMfdjiklFEJUiJKmPwPfbUPYbe3CwqkS4TNvZqsWjp5OY1f9NMWiWyQAAAAATmDeAIA")
BOT_TOKEN = getenv("BOT_TOKEN", "6041305578:AAHifZOeb5UURh-X8APKhBVWCidv8aZvI_A")
BOT_NAME = getenv("BOT_NAME", "Multibot")
API_ID = int(getenv("API_ID", "24086498"))
API_HASH = getenv("API_HASH", "0c459b186767a4634604c740c001c0c3 ")
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://Testingbots01:TESTING1122334455@cluster001.exchcbz.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "soupboy_single")
ALIVE_NAME = getenv("ALIVE_NAME", "present")
BOT_USERNAME = getenv("BOT_USERNAME", "SVDmulti_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "paatu chokar")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "https://t.me/SVD_support_group")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/we_are_universee")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "655594746").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "999"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Soupbot/Newsongposaini")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/d08d6474628be7571f013.png")
