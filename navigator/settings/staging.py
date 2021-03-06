from .base import *

DEBUG = False
ALLOWED_HOSTS = ['selling-online-overseas.export.staging.uktrade.io']
ADMINS = (('David Downes', 'david@downes.co.uk'),)

RESTRICT_IPS = True
ALLOW_AUTHENTICATED = True
ALLOW_ADMIN = True

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
