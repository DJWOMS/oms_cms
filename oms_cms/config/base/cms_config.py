# CMS app
from django.db.models import Q

CMS_APP = [
    # Auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.vk',

    # API
    'rest_framework',
    'django_filters',
    # 'generic_relations',
    # 'corsheaders',
    # DOC
    #'drf_yasg',

    'oms_cms.backend.languages',
    'oms_cms.backend.menu',
    'oms_cms.backend.pages',
    'oms_cms.backend.news',
    'oms_cms.backend.social_networks',
    'oms_cms.backend.contact',
    'oms_cms.backend.utils',
    'oms_cms.backend.search',
    'oms_cms.backend.video',
    'oms_cms.backend.info_block',
    'oms_cms.backend.partners',
    'oms_cms.backend.oms_seo',

    # Editor
    'ckeditor',
    'ckeditor_uploader',

    # 'debug_toolbar',

    # plugins
    'oms_gallery',

    'django_comments',
    'oms_cms.backend.comments',

]

COMMENTS_APP = 'oms_cms.backend.comments'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1


# Email config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = ''
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
# ---------------------

# Allauth
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_UNIQUE = True
# ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True
# ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_VERIFICATION = "optional" #"mandatory"
ACCOUNT_USERNAME_BLACKLIST = ["admin", "administrator", "moderator"]
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_REDIRECT_URL = "/"
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/'
# ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
# -------------------------------------------

# Menu config
MENU_APPS = (
        Q(app_label='pages', model='pages') |
        Q(app_label='news', model='post') |
        Q(app_label='news', model='category') |
        Q(app_label='contact', model='contact') |
        Q(app_label='oms-gallery', model='gallery')
)
# --------------------------------------------

"""Search config
    ("app_label", "model", "field", "field"),
"""
SEARCH_PAGINATE = 5
SEARCH_TEMPLATE = "search/search_list.html"
SEARCH_MODELS = {
    ("pages", "pages", "title"),
    ("news", "category", "name"),
    ("news", "post", "title", "slug"),
}
# --------------------------------------------
