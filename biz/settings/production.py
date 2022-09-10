from .base import *

DEBUG = False
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *
except ImportError:
    pass
