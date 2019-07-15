from django.db import models


class SocialNetworks(models.Model):
    """Модель социальных сетей"""
    title = models.CharField("Название", max_length=50)
    icon_ui = models.CharField("Класс иконки", max_length=500, default='', blank=True)
    icon = models.FileField("Иконка", null=True, blank=True, upload_to="soc_icon/")
    link = models.URLField("URL Соц. сети")

    class Meta:
        verbose_name = "Соц. сеть"
        verbose_name_plural = "Соц. сети"

    def __str__(self):
        return self.title
