"""
OMS CMS project by DJWOMS.
"""

import os
from .base.ckeditor import CKEDITOR_UPLOAD_PATH, CKEDITOR_CONFIGS
from .base.config import *
from .base.jet import *
from .base.api_settings import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Application definition
INSTALLED_APPS = [
    # Custom admin
    'django_grapesjs',
    'jet.dashboard',
    'jet',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # tests
    'django_nose',

    'debug_toolbar',
    'mptt',

    # Editor
    'ckeditor',
    'ckeditor_uploader',

    # Auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.vk',

    # Gallery
    'photologue',
    'sortedm2m',
    # API
    'rest_framework',
    'corsheaders',
    # DOC
    'drf_yasg',
]

INSTALLED_APPS += CMS_APP

THUMBNAIL_HIGH_RESOLUTION = True
USE_JQUERY_UI = True
TABBED_ADMIN_USE_JQUERY_UI = True

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
# NOSE_ARGS = [
#     '--with-coverage',
#     '--cover-package=calendar_of_events',
# ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'oms_cms.config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'oms_cms.backend.languages.context_processors.set_lang',
            ],
        },
    },
]

WSGI_APPLICATION = 'oms_cms.config.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Allauth
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_UNIQUE = True
# ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True
# ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_VERIFICATION = "optional" #"mandatory"
ACCOUNT_USERNAME_BLACKLIST = ["admin", "administrator", "moderator",]
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_REDIRECT_URL = "/"
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/'
# ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True


CORS_ORIGIN_ALLOW_ALL = True

SITE_ID = 1

try:
    from .local_settings import *
except ImportError:
    from .prod_settings import *
