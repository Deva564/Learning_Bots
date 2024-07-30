import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = 11820276
API_HASH = "50a38c2f2c407e7b0c69f950655e92da"
BOT_TOKEN = "7054928677:AAH1c5gZbn8ORE-Djo7Xx2KEItPjTW25FHg"
MONGO_DB_URI = "mongodb+srv://devasachan45:devasachan45@cluster0.tg1kpce.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))
LOG_GROUP_ID = -1002007016158
OWNER_ID = 6492952684

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Learningbots79/Learning_Bots",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/DELED_BED_2024_BSSC_SSC")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/DELED_BED_2024_BSSC_SSC")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQC0XPQAbqrf8vSU2pQSa1n8biwcqrmblqcyvEWHJSzKRQuBHcM474mpoAL1xRHThU9pT4bclZklST_4WThmIzdbgbbaD8X6kUzlKPHWfGYPm0D9SWJ6I5STU5HdkrvLxzrwbrumEkEWG824v98LweG3h1HUay2WWK2Rv9HRhfvb7o2CLUF-yKJcxJz95_2sB8tCk3iGUdH0bT2wTSHxUNHj99eJZphmIhifBbrw6rMszmA1yTiKZnpKMQ8WwbltfWjKKNnfTVOpNM-_BzGk2PRwQun6EbQ9ccemYiT-tLjNkWnjoEW89iYFmIv6zO2DtF91GkAqdTvuXYKtZwcknHJS4RlQAAAAGDAphsAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/9ded6c5fb9dea25bc4ebb.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/9ded6c5fb9dea25bc4ebb.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/9ded6c5fb9dea25bc4ebb.jpg"
STATS_IMG_URL = "https://graph.org/file/9ded6c5fb9dea25bc4ebb.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/9ded6c5fb9dea25bc4ebb.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/9ded6c5fb9dea25bc4ebb.jpg"
STREAM_IMG_URL = "https://graph.org/file/9ded6c5fb9dea25bc4ebb.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/9ded6c5fb9dea25bc4ebb.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/9ded6c5fb9dea25bc4ebb.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/9ded6c5fb9dea25bc4ebb.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/9ded6c5fb9dea25bc4ebb.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/9ded6c5fb9dea25bc4ebb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
