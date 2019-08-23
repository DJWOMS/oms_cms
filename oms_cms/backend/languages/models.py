from django.db import models
from django.urls import reverse


class Lang(models.Model):
    """Модель языков"""
    name = models.CharField("Название", max_length=100, help_text="Пример: Русский")
    slug = models.SlugField("Сокращение названия", max_length=5, help_text="Пример: ru", unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("name_lang", kwargs={"name": self.slug})

    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "Языки"


def get_sentinel_lang():
    """Получить или создать язык по умолчанию"""
    return Lang.objects.get_or_create(name='Русский', slug='ru')[0]


class AbstractLang(models.Model):
    """Абстактная модель для языков"""
    lang = models.ForeignKey(
        Lang,
        verbose_name="Язык",
        on_delete=models.SET(get_sentinel_lang)
    )
