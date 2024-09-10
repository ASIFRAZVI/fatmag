from pathlib import Path, os

# config imports
from .config import (
    internal_apps,
    thirdparty_apps,
    secret_key,
    internal_middlewere,
    allowed_hosts,
    thirdparty_middlewere,
    db_mode,
    media_url,
    media_root,
    dev_db,
    prod_db,
    else_statement,
    debug,
    rest_ramework,
    swagger_config,
    project_parent_directory,
)

# base Dir
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY KEY
SECRET_KEY = secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = debug

# list allowed host
ALLOWED_HOSTS = allowed_hosts

# internal apps
INTERNALAPPS = internal_apps

# Thirdparty apps
THIRDPARTYAPPS = thirdparty_apps

# internal middleware
INTERNALMIDDLEWARE = internal_middlewere

# thirdparty middleware
THIRDPARTYMIDDLEWARE = thirdparty_middlewere


# Application definition
INSTALLED_APPS = (
    [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ]
    + INTERNALAPPS
    + THIRDPARTYAPPS
)

MIDDLEWARE = (
    [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]
    + INTERNALMIDDLEWARE
    + THIRDPARTYMIDDLEWARE
)

ROOT_URLCONF = "fatmag.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "fatmag.wsgi.application"


# DB config
DBconfig = db_mode

# dev_db and prod_db config
if DBconfig == "dev":
    DATABASES = dev_db
elif DBconfig == "prod":
    DATABASES = prod_db
else:
    print(else_statement)


# validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# REST_FRAMEWORK Config
REST_FRAMEWORK = rest_ramework

# SPECTACULAR_SETTINGS config
SPECTACULAR_SETTINGS = swagger_config


# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

# Dajno media
MEDIA_URL = media_url

project_parent_dir = project_parent_directory
# MEDIA_ROOT = os.path.join(project_parent_dir, "media")

# to save in my root file
MEDIA_ROOT = media_root

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
