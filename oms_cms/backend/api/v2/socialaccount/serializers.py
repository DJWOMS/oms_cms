from rest_framework import serializers

from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken
from django.contrib.sites.models import Site
from oms_cms.backend.api.v2.news.serializers import UserSerilizer


class SiteSerializer(serializers.ModelSerializer):
    """Сериализация сайта"""
    class Meta:
        model = Site
        fields = ('id', 'domain', 'name')


class SocialAppExtendedSerializer(serializers.ModelSerializer):
    """Сериализация SocialApp"""
    sites = SiteSerializer(many=True)
    class Meta:
        model = SocialApp
        fields = '__all__'


class SocialAppSerializer(serializers.ModelSerializer):
    """Сериализация SocialApp"""
    class Meta:
        model = SocialApp
        fields = '__all__'


class SocialAppShortSerializer(serializers.ModelSerializer):
    """Сериализация SocialApp"""
    class Meta:
        model = SocialApp
        fields = ('id', 'name')


class SocialAccountExtendedSerializer(serializers.ModelSerializer):
    """Сериализация аккаунта соц. сети"""
    user = UserSerilizer()
    class Meta:
        model = SocialAccount
        fields = '__all__'


class SocialAccountSerializer(serializers.ModelSerializer):
    """Сериализация аккаунта соц. сети"""
    class Meta:
        model = SocialAccount
        fields = '__all__'


class SocialAccountShortSerializer(serializers.ModelSerializer):
    """Сериализация аккаунта соц. сети"""
    user = UserSerilizer()
    class Meta:
        model = SocialAccount
        fields = ('id', 'user')


class SocialTokenSerializer(serializers.ModelSerializer):
    """Сериализация токенов"""
    class Meta:
        model = SocialToken
        fields = '__all__'


class SocialTokenExtendedSerializer(serializers.ModelSerializer):
    """Сериализация токенов"""
    app = SocialAppShortSerializer()
    account = SocialAccountShortSerializer()
    class Meta:
        model = SocialToken
        fields = '__all__'





