from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from oms_cms.backend.languages.models import AbstractLang


class Menu(models.Model):
    """Позиция меню"""
    name = models.CharField(_("Название"), max_length=255)
    status = models.BooleanField(_("Только для зарегистрированных"), default=False)
    published = models.BooleanField(_("Отображать?"), default=True)

    def __str__(self):
        return self.name

    def items(self):
        return self.menuitem_set.all()

    class Meta:
        verbose_name = _("Меню")
        verbose_name_plural = _("Меню")


class MenuItem(MPTTModel, AbstractLang):
    """Элементы меню"""
    title = models.CharField(_("Название пункта меню на сайте"), max_length=255)
    name = models.CharField(_("Название латиницей"), max_length=255)
    icon = models.FileField(_("Иконка"), upload_to="menu/", null=True, blank=True)
    parent = TreeForeignKey(
        'self',
        verbose_name=_("Родительский пункт"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    menu = models.ForeignKey('Menu', verbose_name=_("Меню"), on_delete=models.CASCADE, related_name='menu_items')
    status = models.BooleanField(_("Только для зарегистрированных"), default=False)

    url = models.CharField(_("url на внешний ресурс"), max_length=255, null=True, blank=True)
    anchor = models.CharField(_("Якорь"), max_length=255, null=True, blank=True)

    content_type = models.ForeignKey(
        ContentType,
        verbose_name=_("Ссылка на"),
        limit_choices_to=settings.MENU_APPS,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    object_id = models.PositiveIntegerField(verbose_name=_('Id записи'), default=1, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    sort = models.PositiveIntegerField(_('Порядок'), default=0)
    published = models.BooleanField(_("Отображать?"), default=True)

    def get_anchor(self):
        if self.anchor:
            return "{}/#{}".format(Site.objects.get_current().domain, self.anchor)
        else:
            return False

    def __str__(self):
        return self.name

    content_object.short_description = 'ID'

    class Meta:
        verbose_name = _("Пункт меню")
        verbose_name_plural = _("Пункты меню")

    class MPTTMeta:
        order_insertion_by = ('sort',)

