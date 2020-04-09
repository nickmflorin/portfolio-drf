from .base import *  # noqa

DEBUG = False
DEV = False

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_REGEX_WHITELIST = (r'^(https?://)?([\w\.-]*?)\.nickflorin\.com$',)

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (  # noqa
    'rest_framework.renderers.JSONRenderer',
)
