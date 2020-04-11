#!/usr/bin/env python
import os
import sys


def main():
    # Settings module must be specified in .env file, but can be overridden by
    # explicitly setting ENV variable DJANGO_SETTINGS_MODULE or by specifying
    # as argv --settings=<DJANGO_SETTINGS_MODULE>.
    from portfolio.conf import config
    settings_module = config('DJANGO_SETTINGS_MODULE', required=True)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )
    else:
        execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
