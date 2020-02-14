from rest_framework import serializers

from oms_cms.backend.news.models import Category, Post, FilterPost


class CategorySerializer(serializers.ModelSerializer):
    """Категории статей"""
    class Meta:
        model = Category
        fields = ("id", "name", "slug")


class FilterPostSerializer(serializers.ModelSerializer):
    """Сериализация тегов"""
    class Meta:
        model = FilterPost
        fields = ("title", "name", "icon")


class PostListSerializer(serializers.ModelSerializer):
    """Сериализация новостей"""
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')
    link = serializers.URLField(source="get_absolute_url", read_only=True)
    filters = FilterPostSerializer(many=True)
    #comments_count = serializers.IntegerField(source="get_count_comments", read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "title",
            "subtitle",
            "mini_text",
            "published_date",
            "photo",
            "slug",
            "viewed",
            "filters",
            "image"
           # "comments_count"
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
