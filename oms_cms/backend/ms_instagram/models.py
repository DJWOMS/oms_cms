from django.db import models


class ConfigMSInstagram(models.Model):
    """Модель настроек"""
    name = models.CharField("Имя пользователя", max_length=500)
    client_id = models.CharField("Client ID", max_length=500)
    client_secret = models.CharField("Client secret", max_length=500)
    redirect_uri = models.CharField("Redirect uri", max_length=500)
    access_token = models.CharField("Access token", max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Настройка instagram"
        verbose_name_plural = "Настройки instagram"
