from rest_framework import generics, permissions
from rest_framework import filters as filters_rf

from oms_cms.backend.utils.models import EmailsFeedback
from .serializers import EmailsFeedbackSerializer


class EmailsFeedbackListApi(generics.ListAPIView):
    """Список всех Email для рассылки"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = EmailsFeedback.objects.all()
    serializer_class = EmailsFeedbackSerializer
    filter_backends = [filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    search_fields = ['email', 'id']
    ordering = ['id']


class EmailsFeedbackDeleteUpdateRetrieveWithId(generics.RetrieveUpdateDestroyAPIView):
    """Удаление, изменение и просмотр Email для рассылки (доступ по ID)"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = EmailsFeedback.objects.all()
    lookup_field = 'id'
    serializer_class = EmailsFeedbackSerializer


class EmailsFeedbackCreate(generics.CreateAPIView):
    """Добавление Email для рассылки"""
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = EmailsFeedbackSerializer
    queryset = EmailsFeedback.objects.none()  # Required for DjangoModelPermissions



