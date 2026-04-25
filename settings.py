"""Django settings for the CRUD application."""

import os
from pathlib import Path
from dotenv import load_dotenv

DEBUG = True
"""Django settings for the CRUD application."""

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent

# Templates configuration for Django admin and app templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "crud" / "templates"],
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

# Middleware configuration for Django admin and authentication
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Load environment variables from .env file
load_dotenv(BASE_DIR / ".env")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("DB_NAME", "courses"),
        "USER": os.environ.get("DB_USER", ""),
        "PASSWORD": os.environ.get("DB_PASSWORD", ""),
        "HOST": os.environ.get("DB_HOST", ""),
        "PORT": os.environ.get("DB_PORT", "4000"),
        "OPTIONS": {
            "ssl": {
                "ca": os.environ.get("DB_SSL_CA", str(BASE_DIR / "isrgrootx1.pem")),
            }
        },
    }
}


ROOT_URLCONF = "urls"
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crud",
]

SECRET_KEY = os.environ.get("SECRET_KEY", "")

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Static files (CSS, JavaScript, Images)
# The URL path where static files will be accessible in the browser
STATIC_URL = "static/"

# The absolute path where Django will collect the files for production
STATIC_ROOT = BASE_DIR / "staticfiles"

# Enable WhiteNoise compression and caching
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
