from django.db import models
from django.utils.safestring import mark_safe


class Partners(models.Model):
    """Модель партнеров"""
    picture = models.FileField("Изображение", upload_to="partners/")
    link = models.URLField("Ссылка")

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"

    def __str__(self):
        return self.link

    def get_mini_html(self):
        return mark_safe('<a class="image-picker"><img src="{}"/></a>'.format(self.picture.url))

    mini_html = property(get_mini_html)
    get_mini_html.short_description = 'Изображение'
    get_mini_html.allow_tags = True
