from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from oms_cms.backend.languages.models import AbstractLang


class Menu(models.Model):
    """Позиция меню"""
    name = models.CharField("Название", max_length=255)
    status = models.BooleanField("Только для зарегистрированных", default=False)

    def __str__(self):
        return self.name

    def items(self):
        return self.menuitem_set.all()

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"


class MenuItem(MPTTModel, AbstractLang):
    """Элементы меню"""
    title = models.CharField("Название пункта меню на сайте", max_length=255)
    name = models.CharField("Название латиницей", max_length=255)
    parent = TreeForeignKey(
        'self',
        verbose_name="Родительский пункт",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    menu = models.ForeignKey('Menu', verbose_name="Меню", on_delete=models.CASCADE)
    status = models.BooleanField("Только для зарегистрированных", default=False)

    url = models.CharField("url на внешний ресурс", max_length=255, null=True, blank=True)
    anchor = models.CharField("Якорь", max_length=255, null=True, blank=True)

    # limit = models.Q(app_label='pages', model='pages') | \
    #         models.Q(app_label='news', model='post') | \
    #         models.Q(app_label='news', model='category') | \
    #         models.Q(app_label='contact', model='contact') | \
    #         models.Q(app_label='oms-gallery', model='gallery')

    content_type = models.ForeignKey(
        ContentType,
        verbose_name="Ссылка на",
        # limit_choices_to=limit,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    object_id = models.PositiveIntegerField(verbose_name='Id записи', default=1, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def get_anchor(self):
        if self.anchor:
            return "{}/#{}".format(Site.objects.get_current().domain, self.anchor)
        else:
            return False

    def __str__(self):
        return self.name

    content_object.short_description = 'ID'

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    # class MPTTMeta:
    #     order_insertion_by = ('order', )

