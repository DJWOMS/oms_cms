from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class InfoBlockConfig(AppConfig):
    name = 'oms_cms.backend.info_block'
    verbose_name = _('Инфо блок')
