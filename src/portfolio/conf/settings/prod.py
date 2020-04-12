# from .aws import *  # noqa
from .base import *  # noqa
from .aws import AWS_EC2_IP

DEBUG = False
DEV = False
LIVE = not DEBUG and not DEV

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_REGEX_WHITELIST = (r'^(https?://)?([\w\.-]*?)\.nickflorin\.com$',)

ALLOWED_HOSTS = ['http://%s/' % AWS_EC2_IP, 'https://%s/' % AWS_EC2_IP]

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (  # noqa
    'rest_framework.renderers.JSONRenderer',
)
