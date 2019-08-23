from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import get_script_prefix
from django.utils.encoding import iri_to_uri
from django.utils.translation import gettext_lazy as _

from oms_cms.backend.oms_seo.models import Seo

from oms_cms.backend.languages.models import AbstractLang


class Pages(AbstractLang):
    """Страницы"""
    title = models.CharField(_("Заголовок"), max_length=500)
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
    slug = models.CharField(
        _("URL"),
        max_length=500,
        default="",
        help_text=_("Укажите url"),
        blank=True,
        null=True
    )
    registration_required = models.BooleanField(
        _('Требуется регистрация'),
        help_text=_("Если флажок установлен, только зарегистрированные пользователи смогут просматривать страницу."),
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


