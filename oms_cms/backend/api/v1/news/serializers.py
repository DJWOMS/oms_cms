from rest_framework import serializers

from oms_cms.backend.news.models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    """Категории статей"""
    class Meta:
        model = Category
        fields = ("id", "name", "slug")


class PostSerializer(serializers.ModelSerializer):
    """Сериализация новостей"""
    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "title",
            "subtitle",
            "mini_text",
            "created_date",
            "edit_date",
            "published_date",
            "photo",
            "tag",
            "category",
            "slug",
            "viewed",
            "background_color",
        )


class PostDetailSerializer(serializers.ModelSerializer):
    """Сериализация полной новости"""
    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "title",
            "subtitle",
            "text",
            "created_date",
            "edit_date",
            "published_date",
            "photo",
            "tag",
            "category",
            "slug",
            "viewed",
            "background_color",
        )