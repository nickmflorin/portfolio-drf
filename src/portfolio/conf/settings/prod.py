# from .aws import *  # noqa
from .base import *  # noqa

DEBUG = False
DEV = False
LIVE = not DEBUG and not DEV

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_REGEX_WHITELIST = (r'^(https?://)?([\w\.-]*?)\.nickflorin\.com$',)

ALLOWED_HOSTS = ['http://54.218.224.251/', 'https://54.218.224.251/']

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (  # noqa
    'rest_framework.renderers.JSONRenderer',
)
