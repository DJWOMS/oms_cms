from django import template

from oms_cms.backend.pages.models import Pages

register = template.Library()


@register.simple_tag(takes_context=True)
def for_pages(context):
    """Вывод страниц"""
    return Pages.objects.filter(published=True, lang__slug=context["request"].LANGUAGE_CODE)
