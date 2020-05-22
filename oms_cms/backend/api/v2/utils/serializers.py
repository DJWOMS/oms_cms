from rest_framework import serializers

from oms_cms.backend.utils.models import EmailsFeedback


class EmailsFeedbackSerializer(serializers.ModelSerializer):
    """Сериализация Email для рассылки"""
    class Meta:
        model = EmailsFeedback
        fields = '__all__'


