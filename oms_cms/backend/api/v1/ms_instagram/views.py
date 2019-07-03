from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from oms_cms.backend.ms_instagram.models import ConfigMSInstagram
from oms_cms.backend.ms_instagram.utils import instagram_profile_obj, follow
# from .serializers import


class PhotoListInstagram(APIView):
    """Вывод всех фото из instagram"""
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        if ConfigMSInstagram.objects.filter().exists():
            inst = ConfigMSInstagram.objects.first()
            photos = instagram_profile_obj(inst.name)
        else:
            photos = {}
        return Response(photos)


class FollowInstagram(APIView):
    """Вывод подписчиков instagram"""
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        if ConfigMSInstagram.objects.filter().exists():
            inst = ConfigMSInstagram.objects.first()
            followers = follow(inst.name)
        else:
            followers = {}
        return Response(followers)



