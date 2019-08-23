from django import template

from oms_cms.backend.news.models import Category, Post

register = template.Library()


def get_posts(context, category, order, count):
    """Получаю список статей"""
    if category is not None:
        posts = Post.objects.filter(
            category__name__icontains=category,
            lang__slug=context["request"].LANGUAGE_CODE).order_by(order)
    else:
        posts = Post.objects.filter(lang__slug=context["request"].LANGUAGE_CODE).order_by(order)
    if count is not None:
        posts = posts[:count]
    return posts


def get_categories(context, order, count):
    """Получаю список категорий"""
    categories = Category.objects.filter(published=True, lang__slug=context["request"].LANGUAGE_CODE).order_by(order)
    if count is not None:
        categories = categories[:count]
    return categories


@register.inclusion_tag('base/tags/base_tag.html', takes_context=True)
def category_list(context, order="-name", count=None, template='base/tags/news/categories.html'):
    """template tag вывода категорий"""
    categories = get_categories(context, order, count)
    return {'template': template, "category_list": categories}


@register.simple_tag(takes_context=True)
def for_category_list(context, order="-name", count=None):
    """template tag вывода категорий без шаблона"""
    return get_categories(context, order, count)


@register.inclusion_tag('base/tags/base_tag.html', takes_context=True)
def post_list(context, category=None, order="-published_date", count=None, template='base/tags/news/news_block_tag.html'):
    """Вывод списка статей из категории или всех в шаблон"""
    posts = get_posts(context, category, order, count)
    return {'template': template, "post_list": posts}


@register.simple_tag(takes_context=True)
def for_post_list(context, category=None, order="-published_date", count=None):
    """Вывод списка статей из категории или всех"""
    return get_posts(context, category, order, count)
