from .admin import *  # noqa
from .databases import DATABASES  # noqa
from .logging import LOGGING  # noqa
from .installed_apps import INSTALLED_APPS  # noqa
from .middleware import MIDDLEWARE  # noqa
from .restframework import REST_FRAMEWORK  # noqa
from .paths import (  # noqa
    PROJECT_ROOT, APPS_ROOT, STATIC_ROOT, STATICFILES_DIRS, MEDIA_ROOT)
from .templates import TEMPLATES # noqa
from .urls import ROOT_URLCONF, STATIC_URL, MEDIA_URL, SITE_URL  # noqa

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

SECRET_KEY = 'sc8en5z!!0jc4!mb5mom_ox-ucn)bajz^b%xcich8@0n!rd(n*'
DEBUG = True

ALLOWED_HOSTS = ['*']
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_REGEX_WHITELIST = (
    r'^(https?://)?([\w\.-]*?)\.nickflorin\.com:?[\d]*?$',
    r'^(https?://)?localhost:?[\d]*?$'
)

WSGI_APPLICATION = 'portfolio.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
