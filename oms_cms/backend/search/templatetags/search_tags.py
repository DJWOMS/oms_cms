from django import template

from oms_cms.backend.search.forms import SearchForm

register = template.Library()


@register.simple_tag(takes_context=True)
def get_search_form(context):
    """Вывод формы поиска"""
    return SearchForm()




