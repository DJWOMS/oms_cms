from django.db import models
from django.utils.translation import gettext_lazy as _


class SocialNetworks(models.Model):
    """Модель социальных сетей"""
    title = models.CharField(_("Название"), max_length=50)
    icon_ui = models.CharField(_("Класс иконки"), max_length=500, default='', blank=True)
    icon = models.FileField(_("Иконка"), null=True, blank=True, upload_to="soc_icon/")
    link = models.URLField(_("URL Соц. сети"))

    class Meta:
        verbose_name = _("Соц. сеть")
        verbose_name_plural = _("Соц. сети")

    def __str__(self):
        return self.title
