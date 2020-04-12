from .aws import *  # noqa
from .base import *  # noqa

DEV = True
DEBUG = True
LIVE = not DEBUG and not DEV

ALLOWED_HOSTS = ["*"]
SITE_URL = "https://%s" % AWS_EC2_DOMAIN  # noqa
