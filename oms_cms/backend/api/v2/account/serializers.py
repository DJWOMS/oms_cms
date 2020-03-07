from rest_framework import serializers

from allauth.account.models import EmailAddress
from oms_cms.backend.api.v2.news.serializers import UserSerilizer


class EmailAddressSerialezer(serializers.ModelSerializer):
    """Сериализация email-адресов пользователей"""
    user = UserSerilizer(read_only=True)
    class Meta:
        model = EmailAddress
        fields = ('id', 'email', 'verified', 'primary', 'user')


class EmailAddressEditSerializer(serializers.ModelSerializer):
    """Сериализация email-адресов пользователей"""
    class Meta:
        model = EmailAddress
        fields = '__all__'

