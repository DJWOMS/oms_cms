from rest_framework import serializers
from django.contrib.auth.models import User
from oms_cms.backend.news.models import Category, Post, Tags


class UserSerilizer(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ('id', 'username')


# Post ############################

class TagsInPostSerializer(serializers.ModelSerializer):
    """Сериализация тегов (для отображения в новости)"""
    class Meta:
        model = Tags
        fields = ('id', 'name')


class CategoryInPostSerializer(serializers.ModelSerializer):
    """Сериализация категории (для отображения в новости)"""
    class Meta:
        model = Category
        fields = ('id', 'name')


class PostSerializerRetrieve(serializers.ModelSerializer):
    """Сериализация отдельной новости"""
    author = UserSerilizer(read_only=True)
    tag = TagsInPostSerializer(many=True, read_only=True)
    category = CategoryInPostSerializer()
    user_like = UserSerilizer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    """Сериализация всех новостей"""
    author = UserSerilizer()
    class Meta:
        model = Post
        fields = '__all__'

class PostDeleteUpdateCreateSerializer(serializers.ModelSerializer):
    """Сериализация для удаления/изменения/создания новостей"""
    class Meta:
        model = Post
        fields = '__all__'


# Category ############################

class CategoryPostsSerializer(serializers.HyperlinkedModelSerializer):
    """Сериализация новостей (для отображения в категории)"""
    class Meta:
        model = Post
        fields = ('id', 'title', 'published')


class CategorySerializerRetrieve(serializers.ModelSerializer):
    """Сериализация отдельной категории"""
    category_posts = CategoryPostsSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'lang', 'slug', 'name', 'title', 'description',
                  'template', 'published', 'paginated', 'sort',
                  'lft', 'rght', 'tree_id', 'level', 'parent', 'category_posts')

class CategorySerializer(serializers.ModelSerializer):
    """Сериализация категорий"""
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('id',)


# Tags ############################

class TagsSerializer(serializers.ModelSerializer):
    """Сериализация тегов"""
    class Meta:
        model = Tags
        fields = ('__all__')
        read_only_fields = ('id', )
