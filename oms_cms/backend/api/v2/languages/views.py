from rest_framework import generics, permissions
from rest_framework import filters as filters_rf

from oms_cms.backend.languages.models import AbstractLang
from .serializers import AbstractLangSerializer


class AbstractLangListApi(generics.ListAPIView):
    """Список всех языков"""
    permission_classes = [permissions.AllowAny]
    queryset = AbstractLang.lang
    serializer_class = AbstractLangSerializer
    # filter_backends = [filters_rf.SearchFilter,
    #                    filters_rf.OrderingFilter]
    # search_fields = ['slug', 'lang', 'id']
    # ordering = ['id']



