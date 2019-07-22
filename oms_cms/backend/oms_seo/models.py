from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


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
        verbose_name = "SEO модуль"
        verbose_name_plural = "SEO модуль"


class ConnectSSModel(models.Model):
    """Модель для подключение ПС"""
    name = models.CharField("Имя", max_length=60, help_text="Имя поисковой системы")
    key = models.CharField("Ключ", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подключение ПС"
        verbose_name_plural = "Подключение ПС"


class CounterForSite(models.Model):
    """Счечики и аналитика для сайта"""
    name = models.CharField("Имя", max_length=60, help_text="Имя счетчика")
    code = models.TextField("Код", help_text="Код счетчика или метрики")
    published = models.BooleanField("Включен", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Счетчики и аналитика для сайта"
        verbose_name_plural = "Счетчики и аналитика для сайта"
