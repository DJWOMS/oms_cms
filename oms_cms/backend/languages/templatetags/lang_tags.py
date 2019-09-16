from django import template
from django.conf import settings
from django.urls import translate_url


register = template.Library()


@register.inclusion_tag('base/tags/base_tag.html', takes_context=True)
def list_lang(context, template='base/tags/lang/lang_tag.html'):
    """Вывод списка языков"""
    return {'template': template, "languages": settings.LANGUAGES, "context": context}


@register.simple_tag(takes_context=True)
def for_list_lang(context):
    """Вывод списка языков"""
    return settings.LANGUAGES


@register.simple_tag(takes_context=True)
def change_lang(context, lang):
    """Получение url для перевода"""
    return translate_url(context['request'].path, lang)


@register.simple_tag(takes_context=True)
def get_lang_code(context):
    return context["request"].LANGUAGE_CODE



