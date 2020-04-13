from portfolio.conf import config

from .aws import *  # noqa
from .base import *  # noqa

DEV = True
DEBUG = True
LIVE = not DEBUG and not DEV

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('AWS_RDS_DB_NAME', required=True),
        'USER': config('AWS_RDS_USER', required=True),
        'PASSWORD': config('AWS_RDS_PASSWORD', required=True),
        'HOST': config('AWS_RDS_HOST', required=True),
        'PORT': config('AWS_RDS_PORT', required=True),
    }
}
