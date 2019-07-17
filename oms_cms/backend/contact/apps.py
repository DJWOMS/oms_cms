from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ContactConfig(AppConfig):
    name = 'oms_cms.backend.contact'
    verbose_name = _('Контакты')
