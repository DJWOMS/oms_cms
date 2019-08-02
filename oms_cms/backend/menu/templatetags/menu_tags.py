from functools import wraps
import json

from django import template
from django.utils.safestring import mark_safe

from oms_cms.backend.menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('base/tags/base_tag.html', takes_context=True)
def menu_item(context, menu, template='base/tags/menu/menu-item-tag.html'):
    """Вывод меню в шаблон"""
    return {
        "template": template,
        "items": MenuItem.objects.filter(menu__name=menu, lang__slug=context["request"].session.get("lang"))
    }


@register.simple_tag(takes_context=True)
def for_menu_item(context, menu):
    """Вывод меню без шаблона"""
    return MenuItem.objects.filter(menu__name__icontains=menu, lang__slug=context["request"].session.get("lang"))
