from .aws import *  # noqa
from .base import *  # noqa

DEV = True
DEBUG = True
LIVE = not DEBUG and not DEV

ALLOWED_HOSTS = ["*"]
