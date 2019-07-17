from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class OmsSeoConfig(AppConfig):
    name = 'oms_cms.backend.oms_seo'
    verbose_name = _('SEO')
