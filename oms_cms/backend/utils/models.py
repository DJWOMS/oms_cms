from django.db import models


class EmailsFeedback(models.Model):
    """Email для рассылки"""
    email = models.EmailField("Email")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Email администратора"
        verbose_name_plural = "Emails администраторов"