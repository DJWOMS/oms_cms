from rest_framework import generics, permissions

from oms_cms.backend.info_block.models import InfoBlock
from .serializers import InfoBlockSerializer


class InfoBlockList(generics.ListAPIView):
    """Список информационных блоков"""
    permission_classes = [permissions.AllowAny]
    queryset = InfoBlock.objects.all()
    serializer_class = InfoBlockSerializer
