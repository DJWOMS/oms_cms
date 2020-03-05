from rest_framework import generics, permissions
from rest_framework import filters as filters_rf
from django_filters import rest_framework as filters

from allauth.account.models import EmailAddress
from .serializers import EmailAddressSerialezer, EmailAddressEditSerializer


class EmailAddressListApi(generics.ListAPIView):
    """Список всех email-адресов пользователей"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = EmailAddress.objects.all()
    serializer_class = EmailAddressSerialezer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'verified', 'primary', 'user', 'user__id', 'user__username')
    search_fields = ['id', 'email']
    ordering = ['id']


class EmailAddressRetrieveeleteUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    """Просмотр, изменение и удаление отдельного email-адреса"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = EmailAddress.objects.all()
    lookup_field = 'id'
    serializer_class = EmailAddressEditSerializer


class EmailAddressCreateApi(generics.CreateAPIView):
    """Добавление email-адреса"""
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = EmailAddressEditSerializer
    queryset = EmailAddress.objects.none()

