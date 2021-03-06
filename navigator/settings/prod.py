from .base import *

DEBUG = False
ALLOWED_HOSTS = ['selling-online-overseas.export.great.gov.uk']
ADMINS = (('David Downes', 'david@downes.co.uk'),)

INSTALLED_APPS += [
    'raven.contrib.django.raven_compat'
]

RAVEN_CONFIG = {
    'dsn': os.environ.get('SENTRY_DSN'),
}

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
