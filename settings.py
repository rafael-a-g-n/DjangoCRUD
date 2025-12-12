"""Django settings for the CRUD application."""

import os
from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent

# PostgreSQL
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("DB_NAME", "defaultdb"),
        "USER": os.environ.get("DB_USER", "avnadmin"),
        "PASSWORD": os.environ.get("DB_PASSWORD", ""),
        "HOST": os.environ.get("DB_HOST", "djangotest-ragn-a06e.b.aivencloud.com"),
        "PORT": os.environ.get("DB_PORT", "16579"),
    }
}

INSTALLED_APPS = ("crud",)

SECRET_KEY = os.environ.get("SECRET_KEY", "your-secret-key-here")
