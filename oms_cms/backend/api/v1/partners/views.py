from rest_framework import generics, permissions

from oms_cms.backend.partners.models import Partners
from .serializers import PartnersSerializer


class PartnersList(generics.ListAPIView):
    """Список партнеров"""
    permission_classes = [permissions.AllowAny]
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer
