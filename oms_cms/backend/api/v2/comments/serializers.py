from rest_framework import serializers

from oms_cms.backend.comments.models import OmsComment
from oms_cms.backend.api.v2.news.serializers import UserSerilizer
from oms_cms.backend.api.v2.menu.serializers import ContentTypeSerializer

class OmsCommentChildSerializer(serializers.ModelSerializer):
    """Сериализация дочернего комментария"""
    class Meta:
        model = OmsComment
        fields = ('id', )


class OmsCommentSerializer(serializers.ModelSerializer):
    """Сериализация комментариев"""
    children = OmsCommentChildSerializer(many=True)
    parent = OmsCommentChildSerializer()
    user = UserSerilizer()
    content_type = ContentTypeSerializer()
    class Meta:
        model = OmsComment
        fields = ('id', 'object_pk', 'user', 'user_name', 'user_email',
                  'user_url', 'comment', 'submit_date', 'ip_address', 'is_public',
                  'is_removed', 'update', 'published', 'lft', 'rght', 'tree_id',
                  'level', 'content_type', 'site', 'parent', 'children')


class OmsCommentDeleteUpdateCreateSerializer(serializers.ModelSerializer):
    """Сериализация комментария (изменение/удаление/создание)"""
    class Meta:
        model = OmsComment
        fields = '__all__'

