from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class LanguagesConfig(AppConfig):
    name = 'oms_cms.backend.languages'
    verbose_name = _('Языки')
