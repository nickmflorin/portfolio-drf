import logging

import dj_database_url

from .base import *  # noqa


ALLOWED_HOSTS = ['testserver']

TIME_ZONE = 'UTC'

DATABASES = {
    'default': dj_database_url.parse('sqlite:///%s/db.sqlite3' % PROJECT_ROOT)  # noqa
}

DATABASES['default']['ATOMIC_REQUESTS'] = True

# Disable Logging in Tests
LOGGING['handlers']['portfoliolog'] = LOGGING['handlers']['null']  # noqa
LOGGING['loggers'] = {  # noqa
    '': {
        'handlers': ['null'],
        'level': logging.DEBUG,
        'propagate': False,
    },
}
