from django.db import models


class SpySearch(models.Model):
    """Модель отслеживания запросов поиска"""
    record = models.CharField("Запрос", max_length=1000)
    counter = models.PositiveIntegerField("Количество запросов", default=0)

    class Meta:
        verbose_name = "Запрос поиска"
        verbose_name_plural = "Запросы поиска"

    def __str__(self):
        return "{}".format(self.record)
