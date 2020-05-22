from rest_framework import serializers
from django.contrib.auth.models import User
from oms_gallery.models import Photo, Gallery
from oms_cms.backend.pages.models import Pages, BlockPage


class PagesListSerializer(serializers.ModelSerializer):
    """Сериализация всех страниц"""
    class Meta:
        model = Pages
        fields = '__all__'


class ImageBlockPageSerializer(serializers.HyperlinkedModelSerializer):
    """Сериализация изображения блока информации для старницы"""
    class Meta:
        model = Photo
        fields = ('name', 'image', 'captions', 'create_date', 'slug')


class GalleryBlockPageSerializer(serializers.HyperlinkedModelSerializer):
    """Сериализация галлереи блока информации для старницы"""
    images = ImageBlockPageSerializer(many=True, read_only=True)
    class Meta:
        model = Photo
        fields = ('name', 'captions', 'create_date', 'slug', 'images')


class PageBlockPageSerializer(serializers.ModelSerializer):
    """Сериализация страницы блока информации для старницы"""
    class Meta:
        model = Pages
        fields = ('id',)


class BlockPageSerializer(serializers.HyperlinkedModelSerializer):
    """Сериализация блока информации для старницы"""
    page = PageBlockPageSerializer(read_only=True)
    image = ImageBlockPageSerializer(read_only=True)
    slider = GalleryBlockPageSerializer(read_only=True)
    class Meta:
        model = BlockPage
        fields = ('page', 'id', 'title', 'sub_title', 'description',
                  'video_link', 'video_up', 'name', 'sort',
                  'image', 'slider')


class PagesSerializerRetrieve(serializers.ModelSerializer):
    """Сериализация отдельной страницы"""
    page_blocks = BlockPageSerializer(many=True, read_only=True)
    class Meta:
        model = Pages
        fields = ('id', 'lang', 'slug', 'title', 'sub_title',
                  'text', 'edit_date', 'published_date',
                  'published', 'template', 'registration_required',
                  'page_blocks')


class BlockPageCreateSerializer(serializers.ModelSerializer):
    """Сериализация блока информации для старницы (создание)"""
    class Meta:
        model = BlockPage
        fields = '__all__'