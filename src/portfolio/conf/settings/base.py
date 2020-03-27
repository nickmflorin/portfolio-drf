import os
from pathlib import Path

from .logging import LOGGING  # noqa
from .installed_apps import INSTALLED_APPS  # noqa
from .middleware import MIDDLEWARE  # noqa
from .restframework import REST_FRAMEWORK  # noqa
from .paths import *  # noqa

BASE_DIR = Path(os.path.abspath(__file__)).parents[4]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static Files
STATIC_URL = '/static/'
STATIC_ROOT = "%s/static/" % BASE_DIR

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

SECRET_KEY = 'sc8en5z!!0jc4!mb5mom_ox-ucn)bajz^b%xcich8@0n!rd(n*'
DEBUG = True

ALLOWED_HOSTS = ['*']
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_REGEX_WHITELIST = (
    r'^(https?://)?([\w\.-]*?)\.nickflorin\.com:?[\d]*?$',
    r'^(https?://)?localhost:?[\d]*?$'
)

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'src', 'portfolio', 'app', 'templates'),
            os.path.join(BASE_DIR, 'src', 'portfolio', 'app', 'templates', 'admin')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES['default']['ATOMIC_REQUESTS'] = True

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
