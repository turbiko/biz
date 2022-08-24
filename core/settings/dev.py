from .base import *

# SECURITY WARNING: don't run with debug turned on in production!


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-j6-03_)^4ex5q*nh4l#(y!(b5acsmfp4ue$m@9k#2!fkc+7r8_"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["127.0.0.1", "biz.argentum.ua", "10.1.100.200", "localhost" ]
# CSRF_TRUSTED_ORIGINS = ['biz.argentum.ua']

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
