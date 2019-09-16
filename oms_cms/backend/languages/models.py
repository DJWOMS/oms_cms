from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractLang(models.Model):
    """Абстактная модель для языков"""
    lang = models.CharField(_("Язык"), max_length=7, choices=settings.LANGUAGES, default='en')
    slug = models.SlugField(
        _("url"),
        help_text=_("Укажите url"),
        max_length=500,
        blank=True,
        null=True
    )

    class Meta:
        unique_together = ('lang', 'slug')
        abstract = True
