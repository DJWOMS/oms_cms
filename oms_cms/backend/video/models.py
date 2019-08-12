from django.db import models
from .parse_youtube import parse


class Video(models.Model):
    """Модель видео"""
    title = models.CharField("Заголовок", max_length=500)
    link = models.CharField("Ссылка", max_length=1500)
    slug = models.SlugField("slug", max_length=500, unique=True)
    video_id = models.CharField("Id видео", max_length=1500, default="")
    preview = models.ImageField("Превью", null=True, blank=True)
    duration = models.IntegerField("Продолжительность", default=0)
    url = models.CharField("Сгенерированная ссылка", max_length=1000, default="")

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.link:
            self.preview, self.duration, self.url, self.video_id = parse(self.link)
        super().save(*args, **kwargs)


