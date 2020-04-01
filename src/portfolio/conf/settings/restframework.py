REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    # DO NOT KEEP THIS IN PRODUCTION
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'NON_FIELD_ERRORS_KEY': '__all__',
    # 'UNAUTHENTICATED_USER': False,
}
