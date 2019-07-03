from django.db import models

from photologue.models import Photo, Gallery


class AboutBlock(models.Model):
    """Модель о нас"""
    title = models.CharField("Заголовок", max_length=100)
    desc = models.TextField("Описание", max_length=1000, blank=True)
    slider = models.ForeignKey(
        Gallery,
        verbose_name="Слайдер",
        on_delete=models.CASCADE,
        blank=True,
        null=True)

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

    def __str__(self):
        return self.title
