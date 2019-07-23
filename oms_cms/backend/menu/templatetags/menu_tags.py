from django import template

from oms_cms.backend.menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('base/tags/base_tag.html', takes_context=True)
def menu_item(context, menu, template='base/tags/menu/menu-item-tag.html'):
    return {
        "template": template,
        "items": MenuItem.objects.filter(menu__name=menu, lang__slug=context["request"].session.get("lang"))
    }
