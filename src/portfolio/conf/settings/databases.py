import os

from .paths import PROJECT_ROOT


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
    }
}

DATABASES['default']['ATOMIC_REQUESTS'] = True
