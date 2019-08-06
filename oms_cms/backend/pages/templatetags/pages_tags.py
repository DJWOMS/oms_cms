from django import template

from oms_cms.backend.pages.models import Pages

register = template.Library()


@register.simple_tag
def for_pages():
    """Вывод страниц"""
    return Pages.objects.filter(published=True)
