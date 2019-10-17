from django import template

from oms_cms.backend.pages.models import Pages, BlockPage

register = template.Library()


@register.simple_tag(takes_context=True)
def for_pages(context):
    """Вывод страниц"""
    return Pages.objects.filter(published=True, lang=context["request"].LANGUAGE_CODE)


@register.simple_tag(takes_context=True)
def for_block_page(context, page):
    """Вывод списка блоков страниц"""
    return BlockPage.objects.filter(page=page, page__lang=context["request"].LANGUAGE_CODE)


@register.simple_tag(takes_context=True)
def get_block_page(context, page):
    """Вывод словаря блоков страниц"""
    blocks = BlockPage.objects.filter(page=page, page__lang=context["request"].LANGUAGE_CODE)
    return {block.name: block for block in blocks}


@register.simple_tag(takes_context=True)
def get_list_block_page(context, page):
    """Вывод списка блоков страниц"""
    return BlockPage.objects.filter(page=page, page__lang=context["request"].LANGUAGE_CODE)