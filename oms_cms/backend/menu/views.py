from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from .models import MenuItem

from dal_select2_queryset_sequence.views import Select2QuerySetSequenceView

from queryset_sequence import QuerySetSequence

from oms_cms.backend.news.models import Post
from oms_cms.backend.pages.models import Pages


class LocationAutocompleteView(Select2QuerySetSequenceView):
    def get_queryset(self):
        countries = Post.objects.all()
        cities = Pages.objects.all()

        if self.q:
            countries = countries.filter(continent__icontains=self.q)
            cities = cities.filter(country__name__icontains=self.q)

        # Aggregate querysets
        qs = QuerySetSequence(countries, cities)

        if self.q:
            # This would apply the filter on all the querysets
            qs = qs.filter(name__icontains=self.q)

        # This will limit each queryset so that they show an equal number
        # of results.
        qs = self.mixup_querysets(qs)

        return qs
