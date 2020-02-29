from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from oms_gallery.models import Photo

from oms_cms.backend.languages.models import AbstractLang
from oms_cms.backend.oms_seo.models import Seo


class Category(MPTTModel, AbstractLang):
    """Класс модели категорий сетей"""
    name = models.CharField(_("Название"), max_length=50)
    title = models.CharField(_("Заголовок"), max_length=350, default='', blank=True)
    description = models.TextField(_("Описание"), max_length=1000, default="", blank=True)
    parent = TreeForeignKey(
        'self',
        verbose_name=_("Родительская категория"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    template = models.CharField(_("Шаблон"), max_length=500, default="news/post_list.html")
    published = models.BooleanField(_("Отображать?"), default=True)
    paginated = models.PositiveIntegerField(_("Количество новостей на странице"), default=5)

    sort = models.PositiveIntegerField(_('Порядок'), default=0)

    seo = GenericRelation(Seo)

    class Meta:
        verbose_name = _("Категория новостей")
        verbose_name_plural = _("Категории новостей")
        unique_together = ('lang', 'slug')

    class MPTTMeta:
        order_insertion_by = ('sort',)

    def get_absolute_url(self):
        return reverse('news:list-news', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Tags(models.Model):
    """Класс модели тегов"""
    name = models.CharField(_("Тег"), max_length=50, unique=True)
    slug = models.SlugField(_("url"), unique=True, max_length=100, blank=True, null=True)
    published = models.BooleanField(_("Отображать?"), default=True)

    class Meta:
        verbose_name = _("Тег")
        verbose_name_plural = _("Теги")

    def get_absolute_url(self):
        return reverse('news:tag-news', kwargs={'tag': self.slug})

    def __str__(self):
        return self.name


class FilterPost(models.Model):
    """Фильтры для статей"""
    lang = models.CharField(_("Язык"), max_length=7, choices=settings.LANGUAGES, default='en')
    title = models.CharField(
        _("Название"), max_length=100, help_text=_("Имя которое отображается на сайте")
    )
    name = models.CharField(_("Имя"), max_length=100)
    icon = models.FileField(_("Изображение"), upload_to="filters/", blank=True, null=True)
    icon_inactive = models.FileField(
        _("Изображение не активной иконки"), upload_to="filters/", blank=True, null=True
    )
    icon_ui = models.CharField(
        _("Иконка"), max_length=50, help_text=_("Иконка из вашего UI"), blank=True, null=True
    )
    published = models.BooleanField(_("Отображать?"), default=True)

    class Meta:
        verbose_name = _("Фильтр")
        verbose_name_plural = _("Фильтры")

    def __str__(self):
        return f"{self.title}"


class Post(AbstractLang):
    """Класс модели поста"""
    author = models.ForeignKey(
        User,
        verbose_name=_("Автор"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    title = models.CharField(_("Заголовок"), max_length=500)
    subtitle = models.CharField(_("Под заголовок"), max_length=500, blank=True, null=True)
    mini_text = models.TextField(_("Краткое содержание"), max_length=5000)
    text = models.TextField(_("Полное содержание"), max_length=10000000)
    created_date = models.DateTimeField(_("Дата создания"), auto_now_add=True)
    edit_date = models.DateTimeField(
        _("Дата редактирования"),
        default=timezone.now,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(
        _("Дата публикации"),
        default=timezone.now,
        blank=True,
        null=True
    )
    image = models.ForeignKey(
        Photo,
        verbose_name=_("Главная фотография"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    tag = models.ManyToManyField(Tags, verbose_name=_("Тег"), blank=True)
    category = models.ForeignKey(
        Category,
        verbose_name=_("Категория"),
        on_delete=models.CASCADE,
        related_name='category_posts'
    )
    filters = models.ManyToManyField(FilterPost, verbose_name=_("Фильтр"), blank=True)
    template = models.CharField(_("Шаблон"), max_length=500, default="news/post_detail.html")

    published = models.BooleanField(_("Опубликовать?"), default=True)
    viewed = models.IntegerField(_("Просмотрено"), default=0)
    status = models.BooleanField(_("Для зарегистрированных"), default=False)

    sort = models.PositiveIntegerField(_('Порядок'), default=0)
    like = models.PositiveIntegerField(_('Понравилось'), default=0)
    user_like = models.ManyToManyField(
        User, verbose_name="Кто лайкнул", related_name="users_like", blank=True
    )

    seo = GenericRelation(Seo)

    class Meta:
        verbose_name = _("Новость")
        verbose_name_plural = _("Новости")
        ordering = ["sort", "-published_date"]
        unique_together = ('lang', 'slug')

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    # def get_count_comments(self):
    #     return f"{self.comments.all().count()}"

    def get_category_slug(self):
        return self.category.slug

    def get_category_template(self):
        return self.category.template

    def get_category_paginated(self):
        return self.category.paginated

    def get_absolute_url(self):
        return reverse(
            'news:new-detail', kwargs={'category': self.category.slug, 'post': self.slug}
        )

    def __str__(self):
        return f"{self.title}"

