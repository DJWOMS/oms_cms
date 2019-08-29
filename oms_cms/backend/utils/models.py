from django.db import models
from django.utils.translation import gettext_lazy as _


class EmailsFeedback(models.Model):
    """Email для рассылки"""
    email = models.EmailField("Email")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("Email администратора")
        verbose_name_plural = _("Emails администраторов")
