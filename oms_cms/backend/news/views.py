from datetime import datetime

from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.translation import get_language
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View

from .models import Post


class PostView(ListView):
    """Вывод всех статей из категории или тега"""
    paginate_by = 5

    def get_posts(self):
        return Post.objects.filter(
                lang=get_language(),
                category__published=True,
                published=True,
                published_date__lte=datetime.now())

    def get_queryset(self):
        if self.kwargs.get('slug') is not None:
            post_list = self.get_posts().filter(category__slug=self.kwargs.get('slug'))
            if post_list.exists():
                self.paginate_by = post_list.first().get_category_paginated()
                self.template_name = post_list.first().get_category_template()
            else:
                raise Http404()
        elif self.kwargs.get('tag') is not None:
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

    def get_post(self, request, **kwargs):
        post = get_object_or_404(
            Post,
            lang=get_language(),
            slug=kwargs.get("post"),
            category__published=True,
            published=True,
            published_date__lte=datetime.now()
        )
        return post

    def get(self, request, **kwargs):
        post = self.get_post(request, **kwargs)
        if post.status and request.user.is_authenticated or not post.status:
            post.viewed += 1
            post.save()
            return render(request, post.template, {"post": post})
        else:
            raise Http404

    def post(self, request, **kwargs):
        post = self.get_post(request, **kwargs)
        if request.user in post.user_like.all():
            post.user_like.remove(User.objects.get(id=request.user.id))
            post.like -= 1
        else:
            post.user_like.add(User.objects.get(id=request.user.id))
            post.like += 1
        post.save()
        return HttpResponse(status=201)


