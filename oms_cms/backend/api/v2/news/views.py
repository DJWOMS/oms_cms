from rest_framework import generics, permissions
from rest_framework import filters as filters_rf
from django_filters import rest_framework as filters

from oms_cms.backend.news.models import Category, Post, Tags
from .serializers import TagsSerializer, CategorySerializer, PostSerializerRetrieve, PostListSerializer, \
    CategorySerializerRetrieve, PostDeleteUpdateCreateSerializer


class TagsListApi(generics.ListAPIView):
    """Список всех тегов"""
    permission_classes = [permissions.AllowAny]
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'published')
    search_fields = ['name', 'slug']
    ordering = ['id']


class TagRetrieveWithId(generics.RetrieveAPIView):
    """Просмотр информации об отдельном теге (доступ по ID)"""
    permission_classes = [permissions.AllowAny]
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    lookup_field = 'id'


class TagsDeleteUpdateWithId(generics.RetrieveUpdateDestroyAPIView):
    """Удаление и изменение тега (доступ по ID)"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Tags.objects.all()
    lookup_field = 'id'
    serializer_class = TagsSerializer


class TagsCreate(generics.CreateAPIView):
    """Создание тега"""
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = TagsSerializer
    queryset = Tags.objects.none()  # Required for DjangoModelPermissions


class CategoryListApi(generics.ListAPIView):
    """Список всех категорий"""
    permission_classes = [permissions.AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'lang', 'published', 'tree_id', 'level', 'parent')
    search_fields = ['id', 'name', 'title', 'slug']
    ordering = ['id']


class CategoryRetrieveWithId(generics.RetrieveAPIView):
    """Просмотр информации об отдельной категории (доступ по ID)"""
    permission_classes = [permissions.AllowAny]
    queryset = Category.objects.all()
    lookup_field = 'id'
    serializer_class = CategorySerializerRetrieve


class CategoryDeleteUpdateWithId(generics.RetrieveUpdateDestroyAPIView):
    """Удаление и изменение категории (доступ по ID)"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Category.objects.all()
    lookup_field = 'id'
    serializer_class = CategorySerializer


class CategoryCreate(generics.CreateAPIView):
    """Создание категории"""
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = CategorySerializer
    queryset = Category.objects.none()  # Required for DjangoModelPermissions


class PostList(generics.ListAPIView):
    """Список всех новостей"""
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'lang', 'created_date', 'edit_date', 'published_date', 'published', 'viewed', 'status',
                     'author', 'image', 'category', 'tag', 'filters',
                     'user_like')
    search_fields = ['id', 'title', 'slug']
    ordering = ['id']


class PostRetrieveWithId(generics.RetrieveAPIView):
    """Просмотр информации об отдельной новости (доступ по ID)"""
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializerRetrieve
    lookup_field = 'id'


class PostDeleteUpdateWithId(generics.RetrieveUpdateDestroyAPIView):
    """Удаление и изменение новости (доступ по ID)"""
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Post.objects.all()
    lookup_field = 'id'
    serializer_class = PostDeleteUpdateCreateSerializer



class PostCreate(generics.CreateAPIView):
    """Создание новости"""
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = PostDeleteUpdateCreateSerializer
    queryset = Post.objects.none()  # Required for DjangoModelPermissions
