from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PartnersConfig(AppConfig):
    name = 'oms_cms.backend.partners'
    verbose_name = _('Партнеры')
