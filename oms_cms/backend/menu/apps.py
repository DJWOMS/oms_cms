from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MenuConfig(AppConfig):
    name = 'oms_cms.backend.menu'
    verbose_name = _('Меню')
