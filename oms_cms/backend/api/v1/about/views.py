from rest_framework import generics, permissions

from oms_cms.backend.about.models import AboutBlock
from .serializers import AboutBlockSerializer


class AboutBlockList(generics.ListAPIView):
    """Вывод о нас"""
    permission_classes = [permissions.AllowAny]
    queryset = AboutBlock.objects.all()
    serializer_class = AboutBlockSerializer
