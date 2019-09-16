from django import template

from oms_cms.backend.menu.models import MenuItem

register = template.Library()


def get_menu_item(context, menu):
    """QuerySet menu item"""
    return MenuItem.objects.filter(
            menu__name=menu,
            menu__published=True,
            published=True,
            lang=context["request"].LANGUAGE_CODE
        )


@register.inclusion_tag('base/tags/base_tag.html', takes_context=True)
def menu_item(context, menu, template='base/tags/menu/menu-item-tag.html'):
    """Вывод меню в шаблон"""
    return {
        "template": template,
        "items": get_menu_item(context, menu)
    }


@register.simple_tag(takes_context=True)
def for_menu_item(context, menu):
    """Вывод меню без шаблона"""
    return get_menu_item(context, menu)
