# CMS app
CMS_APP = [
    'oms_cms.backend.languages',
    'oms_cms.backend.menu',
    'oms_cms.backend.pages',
    'oms_cms.backend.news',
    'oms_cms.backend.social_networks',
    'oms_cms.backend.contact',
    'oms_cms.backend.ms_instagram',
    'oms_cms.backend.utils',
    'oms_cms.backend.search',
    'oms_cms.backend.video',
    'oms_cms.backend.info_block',
    'oms_cms.backend.partners',
    'oms_cms.backend.about',
]

LANGUAGE_CODE = 'ru-ru'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = ''
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False