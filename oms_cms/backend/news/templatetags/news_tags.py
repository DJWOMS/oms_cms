from django import template

from oms_cms.backend.news.models import Category, Post

register = template.Library()


@register.inclusion_tag('base/tags/base_tag.html')
def category_list(template='base/tags/news/categories.html'):
    """template tag вывода категорий"""
    categories = Category.objects.filter(published=True)
    return {'template': template, "category_list": categories}


@register.inclusion_tag('base/tags/base_tag.html')
def post_list(category=None, template='base/tags/news/news_block_tag.html'):
    """Вывод списка статей из категории или всех"""
    if category is not None:
        context = Post.objects.filter(category__name__icontains=category)
    else:
        context = Post.objects.all()
    return {'template': template, "post_list": context}


