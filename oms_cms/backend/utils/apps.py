from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class UtilsConfig(AppConfig):
    name = 'oms_cms.backend.utils'
    verbose_name = _('Настройки')
