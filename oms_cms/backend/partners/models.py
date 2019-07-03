from django.db import models


class Partners(models.Model):
    """Модель партнеров"""
    picture = models.FileField("Изображение", upload_to="partners/")
    link = models.URLField("Ссылка")

    class Meta:
        verbose_name = "Пртнер"
        verbose_name_plural = "Пртнеры"

    def __str__(self):
        return self.link

