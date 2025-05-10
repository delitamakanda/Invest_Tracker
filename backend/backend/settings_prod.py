import os
from settings import *

from settings import config, BASE_DIR

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="*", cast=Csv())

# static files cloud storage
STATIC_URL = f"https://storage.googleapis.com/{config('GCS_STATIC_BUCKET')}/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = f"https://storage.googleapis.com/{config('GCS_MEDIA_BUCKET')}/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEBUG = config("DEBUG", default=False, cast=bool)

# cloud sql connection
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': f"/cloudsql/{config('INSTANCE_CONNECTION_NAME')}",
        'PORT': config('DB_PORT'),
    }
}

ADMIN_EMAIL = config('ADMIN_EMAIL')