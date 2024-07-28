import json
import os
from dotenv import load_dotenv

load_dotenv()
DB_HOST = os.environ.get("DB_HOST")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PORT = os.environ.get("DB_PORT")

SECRET_KEY = os.environ.get("SECRET_KEY")
# db schema
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": DB_NAME,
        "USER": DB_USER,
        "PASSWORD": DB_PASSWORD,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
    }
}

DEBUG = True if int(os.environ.get("DEBUG", 1)) else False

ALLOWED_HOSTS = [
    "*",
]

SECRET_KEY = SECRET_KEY
