from django.contrib.sites.models import Site
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractLang(models.Model):
    """Абстактная модель для языков"""
    lang = models.CharField(_("Язык"), max_length=7, choices=settings.LANGUAGES, default='en')
    slug = models.CharField(
        _("url"),
        help_text=_("Укажите url"),
        max_length=500,
        blank=True,
        null=True
    )

    def get_slug_url(self):
        if not self.slug.endswith("/"):
            slash = "/"
        return f"{Site.objects.get_current().domain}/{self.slug}"

    get_slug_url.short_description = 'Site url'
    get_slug_url.allow_tags = True

    class Meta:
        unique_together = ('lang', 'slug')
        abstract = True
