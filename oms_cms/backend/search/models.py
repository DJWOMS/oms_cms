from django.db import models
from django.utils.translation import gettext_lazy as _


class SpySearch(models.Model):
    """Модель отслеживания запросов поиска"""
    record = models.CharField(_("Запрос"), max_length=1000)
    counter = models.PositiveIntegerField(_("Количество запросов"), default=0)

    class Meta:
        verbose_name = _("Запрос поиска")
        verbose_name_plural = _("Запросы поиска")

    def __str__(self):
        return "{}".format(self.record)
