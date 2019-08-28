from django import template
from django.urls import translate_url

from oms_cms.backend.languages.models import Lang

register = template.Library()


@register.inclusion_tag('base/tags/base_tag.html', takes_context=True)
def list_lang(context, template='base/tags/lang/lang_tag.html'):
    """Вывод списка языков"""
    return {'template': template, "languages": Lang.objects.all(), "context": context}


@register.simple_tag(takes_context=True)
def for_list_lang(context):
    """Вывод списка языков"""
    return Lang.objects.all()


@register.simple_tag(takes_context=True)
def change_lang(context, lang):
    return translate_url(context['request'].path, lang)


@register.simple_tag(takes_context=True)
def get_lang_code(context):
    return context["request"].LANGUAGE_CODE



