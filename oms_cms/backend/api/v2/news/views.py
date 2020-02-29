from rest_framework import generics, permissions
from rest_framework import filters as filters_rf
from django_filters import rest_framework as filters

from oms_cms.backend.news.models import Category, Post, Tags
from .serializers import TagsSerializer, CategorySerializer, PostSerializerRetrieve, PostListSerializer, \
    CategorySerializerRetrieve, PostDeleteUpdateCreateSerializer


class TagsListApi(generics.ListAPIView):
    '''Список всех тегов'''
    permission_classes = [permissions.AllowAny]
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'name', 'slug', 'published')
    search_fields = ['id', 'name', 'slug']
    ordering = ['id']


class TagRetrieveWithId(generics.RetrieveAPIView):
    '''Просмотр информации об отдельном теге (доступ через ID)'''
    permission_classes = [permissions.AllowAny]
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    lookup_field = 'id'


class TagRetrieveWithSlug(generics.RetrieveAPIView):
    '''Просмотр информации об отдельном теге (доступ через slug)'''
    permission_classes = [permissions.AllowAny]
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    lookup_field = 'slug'


class TagsDeleteUpdateWithId(generics.RetrieveAPIView,
                             generics.UpdateAPIView,
                             generics.DestroyAPIView):
    '''Удаление и изменение тега (доступ через ID)'''
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Tags.objects.all()
    lookup_field = 'id'
    serializer_class = TagsSerializer


class TagsCreate(generics.CreateAPIView,
                 generics.GenericAPIView):
    '''Создание тега'''
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = TagsSerializer
    queryset = Tags.objects.none()  # Required for DjangoModelPermissions

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryListApi(generics.ListAPIView):
    '''Список всех категорий'''
    permission_classes = [permissions.AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'lang', 'slug', 'name', 'title', 'description',
                     'template', 'published', 'paginated', 'sort',
                     'lft', 'rght', 'tree_id', 'level', 'parent')
    search_fields = ['id', 'name', 'title', 'slug']
    ordering = ['id']


class CategoryRetrieveWithId(generics.RetrieveAPIView):
    '''Просмотр информации об отдельной категории (доступ через ID)'''
    permission_classes = [permissions.AllowAny]
    queryset = Category.objects.all()
    lookup_field = 'id'
    serializer_class = CategorySerializerRetrieve



class CategoryRetrieveWithSlug(generics.RetrieveAPIView):
    '''Просмотр информации об отдельной категории (доступ через slug)'''
    permission_classes = [permissions.AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializerRetrieve
    lookup_field = 'slug'


class CategoryDeleteUpdateWithId(generics.RetrieveAPIView,
                                 generics.UpdateAPIView,
                                 generics.DestroyAPIView):
    '''Удаление и изменение категории (доступ через ID)'''
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Category.objects.all()
    lookup_field = 'id'
    serializer_class = CategorySerializer


class CategoryCreate(generics.CreateAPIView,
                     generics.GenericAPIView):
    '''Создание категории'''
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = CategorySerializer
    queryset = Category.objects.none()  # Required for DjangoModelPermissions


class PostList(generics.ListAPIView):
    '''Список всех новостей'''
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    filter_backends = [filters.DjangoFilterBackend,
                       filters_rf.SearchFilter,
                       filters_rf.OrderingFilter]
    filter_fields = ('id', 'lang', 'slug', 'title', 'subtitle', 'mini_text',
                     'text', 'created_date', 'edit_date', 'published_date',
                     'template', 'published', 'viewed', 'status', 'sort',
                     'like', 'author', 'image', 'category', 'tag', 'filters',
                     'user_like')
    search_fields = ['id', 'title', 'slug']
    ordering = ['id']


class PostRetrieveWithId(generics.RetrieveAPIView):
    '''Просмотр информации об отдельной новости (доступ через ID)'''
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializerRetrieve
    lookup_field = 'id'


class PostRetrieveWithSlug(generics.RetrieveAPIView):
    '''Просмотр информации об отдельной новости (доступ через slug)'''
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializerRetrieve
    lookup_field = 'slug'


class PostDeleteUpdateWithId(generics.RetrieveAPIView,
                             generics.UpdateAPIView,
                             generics.DestroyAPIView):
    '''Удаление и изменение новости (доступ через ID)'''
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Post.objects.all()
    lookup_field = 'id'
    serializer_class = PostDeleteUpdateCreateSerializer


class PostDeleteUpdateWithSlug(generics.RetrieveAPIView,
                               generics.UpdateAPIView,
                               generics.DestroyAPIView):
    '''Удаление и изменение новости (доступ через slug)'''
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = Post.objects.all()
    lookup_field = 'slug'
    serializer_class = PostDeleteUpdateCreateSerializer


class PostCreate(generics.CreateAPIView,
                 generics.GenericAPIView):
    """Создание новости"""
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = PostDeleteUpdateCreateSerializer
    queryset = Post.objects.none()  # Required for DjangoModelPermissions
