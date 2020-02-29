REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser',
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    # 'DEFAULT_FILTER_BACKENDS': [
    #     'django_filters.rest_framework.DjangoFilterBackend'
    # ],

    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        #'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata',
    # 'DEFAULT_PAGINATION_CLASS':
    #     'rest_framework_json_api.pagination.PageNumberPagination',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
    'UPLOADED_FILES_USE_URL': False

}



# JWT_AUTH = {
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(days=2),
#     'JWT_ALLOW_REFRESH': True,
#     'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7)  # default
# }
#
# DJOSER = {
#     'SEND_ACTIVATION_EMAIL': True,
#     # 'SEND_CONFIRMATION_EMAIL': True,
#     'ACTIVATION_URL': 'auth/activate/{uid}/{token}/',
#     'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
#     'PASSWORD_RESET_CONFIRM_URL': 'auth/reset/confirm/{uid}/{token}/',
#     'TOKEN_MODEL': None
# }
