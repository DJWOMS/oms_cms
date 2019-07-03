from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from photologue.models import Gallery

from oms_cms.backend.languages.models import AbstractLang


class Pages(AbstractLang):
    """Страницы"""
    author = models.ForeignKey(
        User,
        verbose_name="Автор",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    title = models.CharField("Заголовок", max_length=500)
    text = RichTextUploadingField("Тест", blank=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        auto_now=True,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField("Дата публикации", blank=True, null=True)
    gallery = models.ForeignKey(
        Gallery,
        verbose_name="Фотографии",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    activate = models.BooleanField("Опубликовать?", default=True)
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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.slug:
            return reverse('page', kwargs={'slug': self.slug})
        else:
            return reverse('page')



