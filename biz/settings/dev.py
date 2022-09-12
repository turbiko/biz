from .base import *
import os

SECRET_KEY = os.environ.get("SECRET_KEY", "@WTREGVw4tgthg536UJET7iujETYJ4e67ujET7ietyj")
DEBUG = os.environ.get("DEBUG", True)

print('DEBUG=', DEBUG)

# ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
CSRF_TRUSTED_ORIGINS = ['https://*.argentum.ua','https://127.0.0.1']


# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

# Database PostgreSQL
if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME":   os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get("SQL_ENGINE"),
            'NAME': os.environ.get("SQL_DATABASE"),
            'USER': os.environ.get("SQL_USER"),
            'PASSWORD': os.environ.get("SQL_PASSWORD"),
            'HOST': os.environ.get("SQL_HOST"),
            'PORT': os.environ.get("SQL_PORT"),
        }
    }

# https://stackoverflow.com/questions/69490806/wagtail-formbuilder-submissions-are-not-sending-emails
if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

try:
    from .local import *
except ImportError:
    pass
