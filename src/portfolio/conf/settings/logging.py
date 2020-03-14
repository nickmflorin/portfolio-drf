import logging
import sys


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {},
    'formatters': {
        'verbose': {
            'format': '[portfolio] %(name)s %(levelname)s [%(module)s:L%(lineno)d; %(funcName)s()]: %(message)s',  # noqa
        },
        'json': {
            '()': 'portfolio.core.logger.JsonLogFormatter',
            'logger_name': 'portfolio'
        },
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'verbose'
        },
        'portfoliolog': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'json',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'root': {
        'handlers': ['portfoliolog'],
        'level': logging.INFO
    },
    'loggers': {
        'django': {
            'handlers': ['portfoliolog'],
            'level': logging.INFO,
            'propagate': True,
        },
        'django.server': {
            'handlers': ['portfoliolog', 'django.server'],
            'level': logging.INFO,
            'propagate': False,
        },
        'portfolio': {
            'handlers': ['portfoliolog'],
            'level': logging.INFO,
            'propagate': False,
        },
        'requests': {
            'level': logging.WARNING
        },
        '': {
            'level': logging.WARNING,
            'handlers': ['portfoliolog', 'console'],
            'propagate': False,
        },
    }
}
