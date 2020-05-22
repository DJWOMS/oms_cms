from django.contrib.sites.models import Site
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import get_script_prefix
from django.utils.encoding import iri_to_uri
from django.utils.translation import gettext_lazy as _
from oms_gallery.models import Photo, Gallery

from oms_cms.backend.oms_seo.models import Seo

from oms_cms.backend.languages.models import AbstractLang


class Pages(AbstractLang):
    """Страницы"""
    title = models.CharField(_("Заголовок"), max_length=500)
    sub_title = models.CharField(_("Подзаголовок"), max_length=500, blank=True, null=True)
    text = models.TextField(_("Текст"), blank=True, null=True)
    edit_date = models.DateTimeField(
        _("Дата редактирования"),
        auto_now=True,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(_("Дата публикации"), blank=True, null=True)
    published = models.BooleanField(_("Опубликовать?"), default=True)
    template = models.CharField(_("Шаблон"), max_length=500, default="pages/home.html")
    registration_required = models.BooleanField(
        _('Требуется регистрация'),
        help_text=_("Если флажок установлен, только зарегистрированные пользователи могут "
                    "просматривать страницу."),
        default=False,
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
        verbose_name = _("Страница")
        verbose_name_plural = _("Страницы")
        unique_together = ('lang', 'slug')


class BlockPage(models.Model):
    """Блок информации для старницы"""
    page = models.ForeignKey(Pages, on_delete=models.CASCADE, related_name='page_blocks')
    image = models.ForeignKey(
        Photo,
        verbose_name=_("Изображение"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    slider = models.ForeignKey(
        Gallery, verbose_name=_("Слайдер"), null=True, blank=True, on_delete=models.CASCADE
    )
    video_link = models.CharField(_("Ссылка на видео"), max_length=1000, blank=True, null=True)
    video_up = models.FileField(_("Видео"), upload_to="block_page/video/", null=True, blank=True)
    background_color = models.CharField(_("Цвет фона"), max_length=30, blank=True, null=True)
    name = models.CharField(_("Имя"), max_length=100, help_text=_("Для обращения в шаблоне"))
    title = models.CharField(_("Заголовок"), max_length=100, blank=True, null=True)
    sub_title = models.CharField(_("Под заголовок"), max_length=100, blank=True, null=True)
    description = models.TextField(_("Описание"), blank=True, null=True)
    sort = models.PositiveIntegerField(_('Порядок'), default=0)

    def __str__(self):
        return f"{self.title} - {self.page}"

    class Meta:
        verbose_name = _("Блок страницы")
        verbose_name_plural = _("Блоки страницы")
        ordering = ["sort"]


