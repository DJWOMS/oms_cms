from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from photologue.models import Photo


class ConvertImage(models.Model):
    """Конвертированые изображения"""
    photo = models.OneToOneField(Photo, verbose_name="Исходное изображение", on_delete=models.CASCADE)
    image_webp = models.ImageField("webp", null=True, blank=True)
    image_j2k = models.ImageField("j2k", null=True, blank=True)

    def __str__(self):
        return "хз"

    class Meta:
        verbose_name = "Конвертированые изображение"
        verbose_name_plural = "Конвертированые изображения"


# @receiver(post_save, sender=Photo)
# def create_convert_img(sender, instance, created, **kwargs):
#     """Сохранение фото"""
#     if created:
#         ConvertImage.objects.create(photo=instance)
#         instance.converitmage.save()


# class EmailsFeedback(models.Model):
#     """Email для рассылки"""
#     email = models.EmailField("Email")
#
#     def __str__(self):
#         return self.email
#
#     class Meta:
#         verbose_name = "Email администратора"
#         verbose_name_plural = "Emails администратора"