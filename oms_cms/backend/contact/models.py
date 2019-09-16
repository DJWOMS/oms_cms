from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from oms_cms.backend.contact.send_mail import send_mail_contact
from oms_cms.backend.languages.models import AbstractLang
from oms_cms.backend.social_networks.models import SocialNetworks


class Contact(AbstractLang):
    """Контакты"""
    name = models.CharField(_("Название"), max_length=100, default=_("Контакты"))
    description = models.TextField(_("Описание"), max_length=5000, blank=True, null=True)
    map = models.CharField(_("Карта"), max_length=10000, blank=True, null=True)

    class Meta:
        verbose_name = _("Контакт")
        verbose_name_plural = _("Контакты")
        unique_together = ('lang', 'slug')

    def __str__(self):
        return "{}".format(self.name)

    def get_contact_fields(self):
        return ContactFields.objects.filter(contact_id=self.id)

    def get_contact_socnet(self):
        return ContactSocNet.objects.filter(contact_soc_id=self.id)


class ContactFields(models.Model):
    """Поля контактов"""
    text = models.CharField(_("Поле 1"), max_length=1000, blank=True)
    text_two = models.CharField(_("Поле 2"), max_length=1000, blank=True)
    icon_ui = models.CharField(_("Класс иконки"), max_length=500, blank=True)
    icon = models.FileField(
        upload_to="icon/",
        verbose_name=_("Иконка"),
        null=True,
        blank=True
    )
    contact = models.ForeignKey(
        Contact,
        related_name="contact_field",
        verbose_name=_("Контакты"),
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("Поле контактов")
        verbose_name_plural = _("Поля контактов")
        ordering = ["id"]

    def __str__(self):
        return self.text


class ContactSocNet(models.Model):
    """Модель соц. сетей"""
    contact_soc = models.ForeignKey(
        Contact,
        verbose_name=_("Контакт"),
        related_name="soc_net",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    your_id = models.CharField(_("Ваша ссылка"), max_length=100, null=True, blank=True)
    link = models.ForeignKey(
        SocialNetworks,
        verbose_name=_("Соц. сеть"),
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _("Соц. сеть")
        verbose_name_plural = _("Соц. сети")

    def __str__(self):
        return "{}".format(self.link)

    def get_link_contact_soc(self):
        return "{}/{}".format(self.link.link, self.your_id)


class Feedback(models.Model):
    """Модель формы обратной связи"""
    full_name = models.CharField(_('ФИО'), max_length=100)
    email = models.EmailField(_('Почта'), max_length=150)
    phone = models.CharField(_('Телефон'), max_length=14)
    subject = models.CharField(_("Тема"), max_length=150)
    message = models.TextField(_('Сообщение'), max_length=1000)
    date = models.DateTimeField(_("Дата"), auto_now_add=True)

    def __str__(self):
        if self.full_name:
            return "{}".format(self.full_name)
        elif self.email:
            return "{}".format(self.email)
        else:
            return "{}".format(self.phone)

    def get_absolute_url(self):
        return reverse('contact:feedback')

    class Meta:
        verbose_name = _("Обратная связь")
        verbose_name_plural = _("Обратные связи")


@receiver(post_save, sender=Feedback)
def send_feedback_email(sender, instance, created, **kwargs):
    """Отправка email"""
    if created:
        full_name = email = phone = subject = message = date = ''
        if instance.full_name is not None:
            full_name = 'ФИО - {}<br>'.format(instance.full_name)
        if instance.email is not None:
            email = 'Email - {}<br>'.format(instance.email)
        if instance.phone is not None:
            phone = 'Номер - {}<br>'.format(instance.phone)
        if instance.subject is not None:
            subject = 'Тема - {}<br>'.format(instance.subject)
        if instance.message is not None:
            message = 'Сообщение: <br> {} <br>'.format(instance.message)
        topic = 'Новое сообщение обратной связи {}'.format(Site.objects.get_current())
        message = """<p>{}{}{}{}{}{}</p>""".format(full_name, email, phone, subject, message, date)
        send_mail_contact(topic, message)
