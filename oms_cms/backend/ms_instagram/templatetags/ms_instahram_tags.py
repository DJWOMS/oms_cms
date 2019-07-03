from django import template

from oms_cms.backend.ms_instagram.models import ConfigMSInstagram
from oms_cms.backend.ms_instagram.utils import *

register = template.Library()


@register.inclusion_tag('base/tags/base_tag.html')
def instagram_photo(name=None, template='base/tags/ms_instagram/instagram_tag.html'):
    """Получение фото из профиля"""
    photos = on_recent()
    return {"template": template, "photos": photos}


@register.inclusion_tag('base/tags/base_tag.html')
def instagram_tag(tag=None, template='base/tags/ms_instagram/instagram_tag.html'):
    """Получение фото по хештегу"""
    photos = get_of_tag(tag)
    return {"template": template, "photos": photos}
