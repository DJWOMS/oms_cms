from rest_framework import serializers

from oms_cms.backend.news.models import Category, Post, Tags


class TagsSerializer(serializers.ModelSerializer):
    '''Сериализация тегов'''
    class Meta:
        model = Tags
        fields = '__all__'
        read_only_fields = ('id', )


class CategorySerializer(serializers.ModelSerializer):
    """Сериализация категорий"""
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ('id',)


class PostSerializer(serializers.ModelSerializer):
    '''Сериализация новостей'''
    class Meta:
        model = Post
        fields = '__all__'
