from datetime import datetime

from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View

from oms_cms.backend.languages.models import Lang
from .models import Post, Comments
from .forms import CommentsForm


class PostView(ListView):
    """Вывод всех статей или из категории"""

    def get_queryset(self):
        if self.kwargs.get('lang', None) is None:
            self.kwargs["lang"] = Lang.objects.get(is_default=True).slug
        if self.kwargs.get('slug') is not None:
            post_list = Post.objects.filter(
                lang__slug__icontains=self.kwargs.get('lang'),
                category__slug=self.kwargs.get('slug'),
                category__published=True,
                published=True,
                published_date__lte=datetime.now())
            if post_list.exists():
                self.paginate_by = post_list.first().get_category_paginated()
                self.template_name = post_list.first().get_category_template()
        else:
            post_list = Post.objects.filter(
                lang__slug__icontains=self.kwargs.get('lang'),
                category__published=True,
                published=True,
                published_date__lte=datetime.now())

        if post_list.exists():
            if not self.request.user.is_authenticated:
                post_list = post_list.filter(status=False)
            return post_list
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
            category__published=True,
            published=True,
            published_date__lte=datetime.now())
        if new.status and request.user.is_authenticated or not new.status:
            new.viewed += 1
            new.save()
            form = CommentsForm()
            return render(request, new.template, {"post": new, "form": form})
        else:
            raise Http404

    # Отправка комментария
    def post(self, request, lang=None, category=None, post=None):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post = Post.objects.get(slug=post)
            form.save()
        return redirect(request.path)


class EditComment(UpdateView):
    """Редактирование комментария"""
    model = Comments
    form_class = CommentsForm
    template_name = 'news/comment_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post.category.slug = self.kwargs.get('category')
        form.instance.post.slug = self.kwargs.get('post')
        self.success_url = Post.objects.get(comments=self.object.id).get_absolute_url()
        form.save()
        return super(EditComment, self).form_valid(form)


class AnswerComment(CreateView):
    """Ответ на комментарий"""
    model = Comments
    form_class = CommentsForm
    template_name = 'news/comment_create.html'

    def post(self, request, *args, **kwargs):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post = Post.objects.get(comments=self.kwargs.get('pk'))
            comm_1 = self.model.objects.get(id=self.kwargs.get('pk'))
            form.text = comm_1.user.username + ', ' + form.text
            form.save()
            form.move_to(comm_1)
            return redirect('new-detail',
                            lang=self.kwargs.get('lang'),
                            category=self.kwargs.get('category'),
                            post=self.kwargs.get('post'))


class DeleteComment(View):
    """Удаление комментария"""
    def get(self, request, pk, lang=None, category=None, post=None):
        comm = get_object_or_404(Comments, id=pk, user=request.user)
        comm.delete()
        return redirect('new-detail', lang=lang, category=category, post=post)
