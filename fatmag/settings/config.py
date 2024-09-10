# internal imports
from pathlib import Path, os

# thirdparty imports
from dotenv import load_dotenv

# load env
load_dotenv()

# base Dir
BASE_DIR = Path(__file__).resolve().parent.parent

# Django secret key
secret_key = os.getenv("SECRET_KEY")

# Debug mode
debug = os.getenv("DEBUG")

# DB mode
db_mode = os.getenv("db_mode")

# internal apps
internal_apps = ["apps.base", "apps.video"]

# Thirdparty apps
thirdparty_apps = [
    "rest_framework",
    "drf_spectacular",
]

# internal middleware
internal_middlewere = []

# thirdparty middleware
thirdparty_middlewere = []

# list allowed host
allowed_hosts = []

# Swagger config
rest_ramework = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

swagger_config = {
    "TITLE": "Fatmag CCExtractor Assignment",
    "DESCRIPTION": "This application Developed using DRF and PostgreSQL,",
}

# DB

# dev_db configuration
dev_db = {
    "default": {
        "ENGINE": os.getenv("DEV_DB_ENGINE"),
        "NAME": os.getenv("DEV_DB_NAME"),
        "USER": os.getenv("DEV_DB_USER"),
        "PASSWORD": os.getenv("DEV_DB_PASSWORD"),
        "HOST": os.getenv("DEV_DB_HOST"),
        "PORT": os.getenv("DEV_DB_PORT"),
    }
}

# prod_db config
prod_db = {
    "default": {
        "ENGINE": os.getenv("PROD_DB_ENGINE"),
        "NAME": os.getenv("PROD_DB_NAME"),
        "USER": os.getenv("PROD_DB_USER"),
        "PASSWORD": os.getenv("PROD_DB_PASSWORD"),
        "HOST": os.getenv("PROD_DB_HOST"),
        "PORT": os.getenv("PROD_DB_PORT"),
    }
}

# else statement
else_statement = "Database is not configured, Please setup the Database!"

# Dajno media
media_url = "/media/"

# main project dir
project_parent_directory = os.path.dirname(BASE_DIR)

# to save in my root file
media_root = os.path.join(project_parent_directory, "media")
