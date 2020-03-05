from rest_framework import generics, permissions
from rest_framework import filters as filters_rf

from oms_cms.backend.partners.models import Partners
from .serializers import PartnersSerializer


class PartnersListApi(generics.ListAPIView):
    """Список всех партнеров"""
    permission_classes = [permissions.AllowAny]
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer
    filter_backends = [filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    search_fields = ['link', 'id']
    ordering = ['id']


class PartnersDeleteUpdateRetrieveWithId(generics.RetrieveUpdateDestroyAPIView):
    """Удаление, изменение и просмотр партнеров (доступ по ID)"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Partners.objects.all()
    lookup_field = 'id'
    serializer_class = PartnersSerializer


class PartnersCreate(generics.CreateAPIView):
    """Создание партнеров"""
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = PartnersSerializer
    queryset = Partners.objects.none()  # Required for DjangoModelPermissions



