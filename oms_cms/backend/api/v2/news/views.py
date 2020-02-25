from rest_framework import generics, permissions, mixins

from django_filters import rest_framework as filters

from oms_cms.backend.news.models import Category, Post, Tags
from .serializers import TagsSerializer, CategorySerializer, PostSerializer


class TagsListApi(generics.ListAPIView):
    '''Список всех тегов'''
    permission_classes = [permissions.AllowAny]
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ('id', 'name', 'slug', 'published')


class TagRetrieveWithId(generics.RetrieveAPIView):
    '''Просмотр информации об отдельном теге (доступ через ID)'''
    permission_classes = [permissions.AllowAny]
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    lookup_field = 'id'


class TagRetrieveWithSlug(generics.RetrieveAPIView):
    '''Просмотр информации об отдельном теге (доступ через ID)'''
    permission_classes = [permissions.AllowAny]
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    lookup_field = 'slug'


class TagsDeleteUpdateWithId(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    '''Удаление и изменение тега (доступ через ID)'''
    permission_classes = [permissions.IsAdminUser]
    queryset = Tags.objects.all()
    lookup_field = 'id'
    serializer_class = TagsSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class TagsDeleteUpdateWithSlug(mixins.RetrieveModelMixin,
                               mixins.UpdateModelMixin,
                               mixins.DestroyModelMixin,
                               generics.GenericAPIView):
    '''Удаление и изменение тега (доступ через slug)'''
    permission_classes = [permissions.IsAdminUser]
    queryset = Tags.objects.all()
    lookup_field = 'slug'
    serializer_class = TagsSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class TagsCreate(mixins.CreateModelMixin,
                 generics.GenericAPIView):
    '''Создание тега'''
    permission_classes = [permissions.IsAdminUser]
    serializer_class = TagsSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryListApi(generics.ListAPIView):
    '''Список всех категорий'''
    permission_classes = [permissions.AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ('id', 'lang', 'slug', 'name', 'title', 'description',
                     'template', 'published', 'paginated', 'sort',
                     'lft', 'rght', 'tree_id', 'level', 'parent')


class CategoryRetrieveWithId(generics.RetrieveAPIView):
    '''Просмотр информации об отдельной категории (доступ через ID)'''
    permission_classes = [permissions.AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


class CategoryRetrieveWithSlug(generics.RetrieveAPIView):
    '''Просмотр информации об отдельной категории (доступ через slug)'''
    permission_classes = [permissions.AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class CategoryDeleteUpdateWithId(mixins.RetrieveModelMixin,
                                 mixins.UpdateModelMixin,
                                 mixins.DestroyModelMixin,
                                 generics.GenericAPIView):
    '''Удаление и изменение категории (доступ через ID)'''
    permission_classes = [permissions.IsAdminUser]
    queryset = Category.objects.all()
    lookup_field = 'id'
    serializer_class = CategorySerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CategoryDeleteUpdateWithSlug(mixins.RetrieveModelMixin,
                               mixins.UpdateModelMixin,
                               mixins.DestroyModelMixin,
                               generics.GenericAPIView):
    '''Удаление и изменение категории (доступ через slug)'''
    permission_classes = [permissions.IsAdminUser]
    queryset = Category.objects.all()
    lookup_field = 'slug'
    serializer_class = CategorySerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CategoryCreate(mixins.CreateModelMixin,
                     generics.GenericAPIView):
    '''Создание категории'''
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CategorySerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostList(generics.ListAPIView):
    '''Список всех новостей'''
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ('id', 'lang', 'slug', 'title', 'subtitle', 'mini_text',
                     'text', 'created_date', 'edit_date', 'published_date',
                     'template', 'published', 'viewed', 'status', 'sort',
                     'like', 'author', 'image', 'category', 'tag', 'filters',
                     'user_like')


class PostRetrieveWithId(generics.RetrieveAPIView):
    '''Просмотр информации об отдельной новости (доступ через ID)'''
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'


class PostRetrieveWithSlug(generics.RetrieveAPIView):
    '''Просмотр информации об отдельной новости (доступ через slug)'''
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class PostDeleteUpdateWithId(mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             generics.GenericAPIView):
    '''Удаление и изменение статей (доступ через ID)'''
    permission_classes = [permissions.IsAdminUser]
    queryset = Post.objects.all()
    lookup_field = 'id'
    serializer_class = PostSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PostDeleteUpdateWithSlug(mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin,
                             generics.GenericAPIView):
    '''Удаление и изменение статей (доступ через slug)'''
    permission_classes = [permissions.IsAdminUser]
    queryset = Post.objects.all()
    lookup_field = 'slug'
    serializer_class = PostSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PostCreate(mixins.CreateModelMixin,
                 generics.GenericAPIView):
    '''Создание категории'''
    permission_classes = [permissions.IsAdminUser]
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
