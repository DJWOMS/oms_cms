from django.shortcuts import render
from django.views.generic import ListView

from .models import SpySearch


class SearchPost(ListView):
    """Поиск на сайте"""
    paginate_by = 5
    template_name = "blog/post-list.html"

    def get_queryset(self):
        # query = Post.objects.filter(title__icontains=self.request.GET.get('q'))

        question = self.request.GET.get('q')
        rec, a = SpySearch.objects.get_or_create(record=question)
        rec.counter += 1
        rec.save()
        return query
