from django import template

from oms_cms.backend.partners.models import Partners

register = template.Library()


@register.simple_tag()
def all_partners():
    """Вывод списка всех партнеров"""
    return Partners.objects.all()


