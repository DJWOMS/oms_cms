from datetime import datetime

from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.base import View

from oms_cms.backend.languages.models import Lang
from .models import Post


class PostView(ListView):
    """Вывод всех статей или из категории"""
    def get_queryset(self):
        if self.kwargs.get('lang', None) is None:
            self.kwargs["lang"] = Lang.objects.get(is_default=True).slug
        if self.kwargs.get('slug') is not None:
            post_list = Post.objects.filter(
                lang__slug__icontains=self.kwargs.get('lang'),
                category__slug=self.kwargs.get('slug'),
                category__active=True,
                published=True,
                published_date__lte=datetime.now())
        else:
            post_list = Post.objects.filter(
                lang__slug__icontains=self.kwargs.get('lang'),
                category__active=True,
                published=True,
                published_date__lte=datetime.now())

        if self.request.user.is_authenticated:
            posts = post_list
        else:
            posts = post_list.filter(status=False)

        if posts.exists():
            self.paginate_by = posts.first().get_category_paginated()
            self.template_name = posts.first().get_category_template()
            return posts
        else:
            raise Http404()


class PostDetail(View):
    """Вывод полной новости"""
    def get(self, request, lang=None, category=None, post=None):
        if lang is None:
            lang = Lang.objects.get(is_default=True).slug
        new = get_object_or_404(
            Post,
            lang__slug__icontains=lang,
            slug=post,
            category__active=True,
            published=True,
            published_date__lte=datetime.now())
        if new.status and request.user.is_authenticated or not new.status:
            new.viewed += 1
            new.save()
            return render(request, new.template, {"post": new})
        else:
            raise Http404


