# from rest_framework import generics, permissions
#
# from photologue.models import Gallery
# from .serializers import GallerySerializer
#
#
# class GalleryList(generics.ListAPIView):
#     """Список галерей"""
#     permission_classes = [permissions.AllowAny]
#     queryset = Gallery.objects.all()
#     serializer_class = GallerySerializer
#
#
# class GallerySingle(generics.RetrieveAPIView):
#     """Вывод одной галереи по slug"""
#     permission_classes = [permissions.AllowAny]
#     lookup_field = 'slug'
#     queryset = Gallery.objects.all()
#     serializer_class = GallerySerializer
