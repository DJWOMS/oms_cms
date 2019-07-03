from django import template

from oms_cms.backend.languages.models import Lang

register = template.Library()


@register.inclusion_tag('base/tags/base_tag.html')
def list_lang(template='base/tags/lang/lang_tag.html'):
    """Вывод списка языков"""
    return {'template': template, "languages": Lang.objects.all()}



