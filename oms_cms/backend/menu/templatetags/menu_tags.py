from django import template

from oms_cms.backend.menu.models import MenuItem, ItemMenuLang

register = template.Library()


@register.inclusion_tag('base/tags/menu-item-tag.html', takes_context=True)
def menu_item(context, menu, ul=None, li=None, a=None):
    # item = ItemMenuLang.objects.filter(lang__slug=context["request"].session.get("lang"))
    return {
        # "items": MenuItem.objects.filter(menu__slug=menu, parent__isnull=True, itemmenulang__in=item),
        "items": ItemMenuLang.objects.filter(
            item__menu__slug=menu,
            item__parent__isnull=True,
            lang__slug=context["request"].session.get("lang")
        ),
        "ul": ul,
        "li": li,
        "a": a
    }
