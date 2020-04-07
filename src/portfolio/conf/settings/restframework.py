REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'NON_FIELD_ERRORS_KEY': '__all__',
    # 'UNAUTHENTICATED_USER': False,
}
