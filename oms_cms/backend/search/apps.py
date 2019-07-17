from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SearchConfig(AppConfig):
    name = 'oms_cms.backend.search'
    verbose_name = _('Поиск')
