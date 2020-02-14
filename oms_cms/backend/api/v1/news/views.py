from rest_framework import generics, permissions

from oms_cms.backend.news.models import Category, Post
from .serializers import CategorySerializer, PostListSerializer, PostDetailSerializer


class CategoryList(generics.ListAPIView):
    """Список всех категорий"""
    permission_classes = [permissions.AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostList(generics.ListAPIView):
    """Список новостей из категории"""
    permission_classes = [permissions.AllowAny]
    serializer_class = PostListSerializer

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.request.get("category_slug"))


class PostDetail(generics.RetrieveAPIView):
    """Полная статья"""
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
