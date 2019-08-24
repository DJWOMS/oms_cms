from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CommentsConfig(AppConfig):
    name = 'oms_cms.backend.comments'
    verbose_name = _('Комментарии')
