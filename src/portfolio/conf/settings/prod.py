from portfolio.conf import config

from .aws import *  # noqa
from .base import *  # noqa

DEBUG = False
DEV = False
LIVE = not DEBUG and not DEV

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_REGEX_WHITELIST = (r'^(https?://)?([\w\.-]*?)\.nickflorin\.com$',)

ALLOWED_HOSTS = [
    'http://%s' % AWS_EC2_DOMAIN,  # noqa
    'http://%s' % AWS_EC2_DOMAIN,  # noqa
    AWS_EC2_DOMAIN,  # noqa
    AWS_EC2_IP_ADDRESS,  # noqa

]

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (  # noqa
    'rest_framework.renderers.JSONRenderer',
)

SITE_URL = "https://%s" % AWS_EC2_DOMAIN  # noqa

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
