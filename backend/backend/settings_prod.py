import os

from .settings import *
from decouple import config

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
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': f'/cloudsql/{os.environ["INSTANCE_CONNECTION_NAME"]}',
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

ADMIN_EMAIL = config('ADMIN_EMAIL', default='admin@example.com')