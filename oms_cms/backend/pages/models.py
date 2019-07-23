from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse

from oms_cms.backend.oms_seo.models import Seo

from oms_cms.backend.languages.models import AbstractLang


class Pages(AbstractLang):
    """Страницы"""
    title = models.CharField("Заголовок", max_length=500)
    text = models.TextField("Текст", blank=True, null=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now=True,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField("Дата публикации", blank=True, null=True)
    published = models.BooleanField("Опубликовать?", default=True)
    template = models.CharField("Шаблон", max_length=500, default="pages/home.html")
    slug = models.SlugField(
        "URL",
        max_length=500,
        default="",
        help_text="Укажите url",
        unique=True,
        blank=True,
        null=True
    )

    seo = GenericRelation(Seo)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.slug:
            return reverse('page_slug', kwargs={'slug': self.slug})
        else:
            return reverse('page')

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"


