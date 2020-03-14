"""
Monkey patch Django's DEBUG error screen to hide sensitive META variables

Django automatically sanitizes the Settings section of it's debug screen,
but doesn't do the same to the META section, even though it contains
environment variables with passwords, API keys, etc. There is an open ticket
to resolve this (https://code.djangoproject.com/ticket/23004) but it's been
open for 5 years.
"""

from django.views import debug


def monkey_patch_technical_500_response(technical_500_response):
    def patched_technical_500_response(request, *args, **kwargs):
        for key, value in request.META.items():
            # Use the same logic Django applies to sanitize sensitive
            # variables in it's `settings` to request.META
            request.META[key] = debug.cleanse_setting(key, value)
        return technical_500_response(request, *args, **kwargs)
    return patched_technical_500_response


debug.technical_500_response = monkey_patch_technical_500_response(
    debug.technical_500_response)
