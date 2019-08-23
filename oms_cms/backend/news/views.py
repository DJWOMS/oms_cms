from datetime import datetime

from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View

from .models import Post


class PostView(ListView):
    """Вывод всех статей из категории или тега"""

    def get_posts(self):
        return Post.objects.filter(
                lang__slug__icontains=self.request.LANGUAGE_CODE,
                category__published=True,
                published=True,
                published_date__lte=datetime.now())

    def get_queryset(self):
        if self.kwargs.get('slug') is not None:
            post_list = self.get_posts().filter(category__slug=self.kwargs.get('slug'))
            if post_list.exists():
                self.paginate_by = post_list.first().get_category_paginated()
                self.template_name = post_list.first().get_category_template()
        if self.kwargs.get('tag') is not None:
            post_list = self.get_posts().filter(tag__slug=self.kwargs.get('tag'))
        else:
            post_list = self.get_posts()

        if post_list.exists():
            if not self.request.user.is_authenticated:
                post_list = post_list.filter(status=False)
            return post_list
        else:
            raise Http404()


class PostDetail(View):
    """Вывод полной новости"""

    def get(self, request, **kwargs):
        new = get_object_or_404(
            Post,
            lang__slug=request.LANGUAGE_CODE,
            slug=kwargs.get("post"),
            category__published=True,
            published=True,
            published_date__lte=datetime.now())
        if new.status and request.user.is_authenticated or not new.status:
            new.viewed += 1
            new.save()
            return render(request, new.template, {"post": new})
        else:
            raise Http404
