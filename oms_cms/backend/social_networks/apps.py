from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SocialNetworksConfig(AppConfig):
    name = 'oms_cms.backend.social_networks'
    verbose_name = _('Социальные сети')
