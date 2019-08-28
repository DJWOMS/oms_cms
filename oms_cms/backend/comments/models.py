from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.utils.translation import ugettext_lazy as _
from django_comments.abstracts import CommentAbstractModel


class OmsComment(CommentAbstractModel, MPTTModel):
    parent = TreeForeignKey(
        "self",
        verbose_name=_("Родительский комментарий"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children')
    update = models.DateTimeField(_("Изменен"), auto_now=True)
    published = models.BooleanField(_("Отображать?"), default=True)

    # def delete_comment(self):
    #     return reverse('delete_comment', kwargs={'pk': self.id})
    #
    # def edit_comment(self):
    #     return reverse('edit_comment', kwargs={'pk': self.id})
    #
    # def answer_comment(self):
    #     return reverse('answer_comment', kwargs={'pk': self.id})
