from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Lang(models.Model):
    """Модель языков"""
    name = models.CharField(_("Название"), max_length=100, help_text=_("Пример: Русский"))
    slug = models.SlugField(_("Сокращение названия"), max_length=5, help_text=_("Пример: ru"), unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("languages:name_lang")

    class Meta:
        verbose_name = _("Язык")
        verbose_name_plural = _("Языки")


def get_sentinel_lang():
    """Получить или создать язык по умолчанию"""
    return Lang.objects.get_or_create(name='Русский', slug='ru')[0]


class AbstractLang(models.Model):
    """Абстактная модель для языков"""
    lang = models.ForeignKey(
        Lang,
        verbose_name=_("Язык"),
        on_delete=models.SET(get_sentinel_lang)
    )
