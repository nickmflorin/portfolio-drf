import os
from .base import *  # noqa
from .paths import PROJECT_ROOT


DEBUG = True
DEV = False

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/')

ALLOWED_HOSTS = ["*"]
