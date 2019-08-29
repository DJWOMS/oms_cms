from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _


class Seo(models.Model):
    """SEO модуль"""
    title_page = models.CharField("Title", max_length=60)
    description_page = models.CharField("Description", max_length=150)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return self.title_page

    class Meta:
        verbose_name = _("SEO модуль")
        verbose_name_plural = _("SEO модуль")


class ConnectSSModel(models.Model):
    """Модель для подключение ПС"""
    name = models.CharField(_("Имя"), max_length=60, help_text=_("Имя поисковой системы"))
    key = models.CharField(_("Ключ"), max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Подключение ПС")
        verbose_name_plural = _("Подключение ПС")


class CounterForSite(models.Model):
    """Счечики и аналитика для сайта"""
    name = models.CharField(_("Имя"), max_length=60, help_text=_("Имя счетчика"))
    code = models.TextField(_("Код"), help_text=_("Код счетчика или метрики"))
    published = models.BooleanField(_("Включен"), default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Счетчики и аналитика для сайта")
        verbose_name_plural = _("Счетчики и аналитика для сайта")
