# coding=utf-8
import os
from django.utils.translation import gettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b0!c@b!o_#F$^#@@!D@bv%#yhxs=qm@ana6l2$n=!p1ejm@'

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'omsCMS',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

# INTERNAL_IPS = '127.0.0.1'

DEFAULT_FROM_EMAIL = 'info@skyp-auto.ru'
EMAIL_HOST_PASSWORD = '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'

LANGUAGE_CODE = 'ru'

LANGUAGES = (
    ('en', _('English')),
    ('ru', _('Russian')),
)