from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import get_script_prefix
from django.utils.encoding import iri_to_uri

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
    slug = models.CharField(
        "URL",
        max_length=500,
        default="",
        help_text="Укажите url",
        blank=True,
        null=True
    )

    seo = GenericRelation(Seo)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = "/"
        if not f"{self.slug}".startswith("/"):
            self.slug = "/" + self.slug
        if not self.slug.endswith("/"):
            self.slug += "/"
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return iri_to_uri(get_script_prefix().rstrip('/') + self.slug)

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"


