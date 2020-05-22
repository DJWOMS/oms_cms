from rest_framework import generics, permissions
from rest_framework import filters as filters_rf
from django_filters import rest_framework as filters

from oms_cms.backend.search.models import SpySearch
from .serializers import SpySearchSerializer


class SpySearchListApi(generics.ListAPIView):
    """Список всех запросов"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = SpySearch.objects.all()
    serializer_class = SpySearchSerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    search_fields = ['record']
    ordering = ['-counter']



