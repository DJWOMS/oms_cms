from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _


class OpenGraph(models.Model):
    """OpenGraph модуль"""
    title_page = models.CharField("Title", max_length=100, blank=True, null=True)
    description_page = models.CharField("Description", max_length=250, blank=True, null=True)
    type_page = models.CharField("Type", max_length=60, blank=True, null=True)
    image_page = models.ImageField("Image", upload_to="open_graph/", blank=True, null=True)
    url_page = models.CharField("URL", max_length=1000, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return f'{self.title_page}'

    class Meta:
        verbose_name = _("OpenGraph модуль")
        verbose_name_plural = _("OpenGraph модуль")
