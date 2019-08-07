from django import template

from oms_cms.backend.news.models import Category, Post, Comments

register = template.Library()


@register.inclusion_tag('base/tags/base_tag.html')
def category_list(template='base/tags/news/categories.html'):
    """template tag вывода категорий"""
    categories = Category.objects.filter(published=True)
    return {'template': template, "category_list": categories}


@register.simple_tag()
def for_category_list():
    """template tag вывода категорий без шаблона"""
    return Category.objects.filter(published=True)


@register.inclusion_tag('base/tags/base_tag.html')
def post_list(category=None, template='base/tags/news/news_block_tag.html'):
    """Вывод списка статей из категории или всех в шаблон"""
    if category is not None:
        context = Post.objects.filter(category__name__icontains=category)
    else:
        context = Post.objects.all()
    return {'template': template, "post_list": context}


@register.simple_tag()
def for_post_list(category=None):
    """Вывод списка статей из категории или всех"""
    if category is not None:
        context = Post.objects.filter(category__name__icontains=category)
    else:
        context = Post.objects.all()
    return context


@register.inclusion_tag('base/tags/base_tag.html', takes_context=True)
def comments_show(context, pk, template='base/tags/news/comments.html'):
    """Вывод комментариев к статье в шаблон"""
    return {"template": template, "comments": Comments.objects.filter(post_id=pk, published=True), "context": context}


@register.simple_tag
def for_comments(pk):
    """Вывод комментариев к статье"""
    return Comments.objects.filter(post_id=pk, published=True)
