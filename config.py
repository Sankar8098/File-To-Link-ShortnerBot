
import os


class config(object):
	API_ID = int(os.environ.get("API_ID", "23990433"))
	API_HASH = os.environ.get("API_HASH", "e6c4b6ee1933711bc4da9d7d17e1eb20")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "6119758281:AAFNCl4gzd-1w957bRKEhjb6kW1JnaDZm3U")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "File_To_Links1_Bot")
	CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001828551401"))
	SUPPORT_GROUP = os.environ.get("SUPPORT_CHAT", "TheDeadlyBots")
	SUPPORT_CHANNEL = os.environ.get("SUPPORT_CHANNEL", "TheBotUpdates")
        BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
        SHORTNER_SITE = os.environ.get("SHORTNER_SITE", "https://dalink.in")
        API_KEY = os.environ.get("API_KEY", "8d8be4101ae30e933d02af13f18a2acaa8f4a97c")
