from django.db import models
from django.utils.translation import gettext_lazy as _

from .parse_youtube import parse


class Video(models.Model):
    """Модель видео"""
    title = models.CharField(_("Заголовок"), max_length=500)
    link = models.CharField(_("Ссылка"), max_length=1500)
    slug = models.SlugField(_("slug"), max_length=500, unique=True)
    video_id = models.CharField(_("Id видео"), max_length=1500, default="")
    preview = models.ImageField(_("Превью"), null=True, blank=True)
    duration = models.IntegerField(_("Продолжительность"), default=0)
    url = models.CharField(_("Сгенерированная ссылка"), max_length=1000, default="")

    class Meta:
        verbose_name = _("Видео")
        verbose_name_plural = _("Видео")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.link:
            self.preview, self.duration, self.url, self.video_id = parse(self.link)
        super().save(*args, **kwargs)


