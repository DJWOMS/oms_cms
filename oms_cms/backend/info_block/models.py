from django.db import models
from django.utils.translation import gettext_lazy as _
from oms_gallery.models import Gallery

from oms_cms.backend.languages.models import AbstractLang


class InfoBlock(AbstractLang):
    """Модель инфо блока"""
    title = models.CharField(_("Заголовок"), max_length=100)
    sub_title = models.CharField(_("Под заголовок"), max_length=100, blank=True, null=True)
    description = models.TextField(_("Описание"), max_length=1000, blank=True)
    slider = models.ForeignKey(
        Gallery,
        verbose_name=_("Слайдер"),
        on_delete=models.CASCADE,
        blank=True,
        null=True)

    class Meta:
        verbose_name = _("Инфо блок")
        verbose_name_plural = _("Инфо блок")

    def __str__(self):
        return self.title
