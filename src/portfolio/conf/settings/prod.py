from .aws import *  # noqa
from .base import *  # noqa

DEBUG = False
DEV = False
LIVE = not DEBUG and not DEV

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_REGEX_WHITELIST = (r'^(https?://)?([\w\.-]*?)\.nickflorin\.com$',)

ALLOWED_HOSTS = ['portfolio-api.us-east-1.elasticbeanstalk.com']

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (  # noqa
    'rest_framework.renderers.JSONRenderer',
)
