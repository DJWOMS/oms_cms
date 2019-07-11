from django.contrib.sites.models import Site
from django.core.mail import send_mail, BadHeaderError

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from photologue.models import Photo

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

#from oms_cms.backend.contact.send_mail import send_mail_contact

from oms_cms.backend.social_networks.models import SocialNetworks
from oms_cms.config import settings


class Contact(models.Model):
    """Контакты"""
    SECTIONS = (
        ("header", "верх"),
        ("left", "лево"),
        ("right", "право"),
        ("footer", "низ"),
        ("top_menu", "верхнее меню"),
    )
    name = models.CharField("Название", max_length=100, default="Контакты")
    desk_cont = models.TextField("Описание", max_length=5000, default="", blank=True)
    map = models.CharField("Карта", max_length=10000, blank=True)
    section = models.CharField(
        "Расположение",
        max_length=10,
        choices=SECTIONS,
        null=True,
        unique=True
    )
    slug = models.SlugField("URL", max_length=100, unique=True)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return "{}".format(self.name)

    # def get_absolute_url(self):
    #     return reverse('member', kwargs={'slug': self.slug})

    def get_contact_fields(self):
        return ContactFields.objects.filter(contact_id=self.id)

    def get_contact_socnet(self):
        return ContactSocNet.objects.filter(contact_soc_id=self.id)


class ContactFields(models.Model):
    """Поля контактов"""
    TYPE = (
        ("email", "email"),
        ("phone", "телефон"),
        ("address", "адрес"),
        ("time", "время"),
        ("info", "информация"),
        ("other", "другое"),
    )
    text = models.CharField("Поле 1", max_length=1000, blank=True)
    text_two = models.CharField("Поле 2", max_length=1000, default='', blank=True)
    icon_ui = models.CharField("Класс иконки", max_length=500, default='', blank=True)
    type = models.CharField("Тип данных", max_length=10, choices=TYPE)
    icon = models.ForeignKey(
        Photo,
        verbose_name="Иконка",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    contact = models.ForeignKey(
        Contact,
        related_name="contact_field",
        verbose_name="Контакты",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Контакт поле"
        verbose_name_plural = "Контакты поля"
        ordering = ["id"]

    def __str__(self):
        return self.text


class ContactSocNet(models.Model):
    """Модель соц. сетей для участников"""
    contact_soc = models.ForeignKey(
        Contact,
        verbose_name="Контакт",
        related_name="soc_net",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    your_id = models.CharField("Ваша ссылка", max_length=100, null=True, blank=True)
    link = models.ForeignKey(
        SocialNetworks,
        verbose_name="Соц. сеть",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Соц. сеть"
        verbose_name_plural = "Соц. сети"

    def __str__(self):
        return "{}".format(self.link)

    def get_link_contact_soc(self):
        return "{}/{}".format(self.link.link, self.your_id)


class Feedback(models.Model):
    """Модель формы обратной связи"""
    # TODO: Убрать null=True и добавить сериализаторы для отправки email и телефона
    full_name = models.CharField("ФИО", max_length=500, null=True)
    email = models.EmailField("Email", null=True, blank=True)
    tel = models.CharField("Тел.", max_length=20, default=0)
    theme = models.CharField("Тема", max_length=500, null=True, blank=True)
    message = models.TextField("Сообщение", max_length=1500, null=True, blank=True)
    section = models.CharField("Модуль", max_length=150, default='', null=True, blank=True)

    def __str__(self):
        if self.full_name:
            return "{}".format(self.full_name)
        elif self.email:
            return "{}".format(self.email)
        else:
            return "{}".format(self.tel)

    def get_absolute_url(self):
        return reverse('add_feedback')

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратные связи"


class EmailsFeedback(models.Model):
    """Email для рассылки"""
    email = models.EmailField("Email")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Email администратора"
        verbose_name_plural = "Emails администратора"


@receiver(post_save, sender=Feedback)
def send_feedback_email(sender, instance, created, **kwargs):
    """Отправка email"""
    if created:
        section = name = email = phone = theme = comment = ''
        if instance.section is not None:
            section = 'Модуль - {}<br>'.format(instance.section)
        if instance.full_name is not None:
            name = 'ФИО - {}<br>'.format(instance.full_name)
        if instance.email is not None:
            email = 'Email - {}<br>'.format(instance.email)
        if instance.tel is not None:
            phone = 'Номер - {}<br>'.format(instance.tel)
        if instance.theme is not None:
            theme = 'Тема - {}<br>'.format(instance.theme)
        if instance.message is not None:
            comment = 'Сообщение: <br> {}'.format(instance.message)
        subject = 'Новое сообщение обратной связи {}'.format(Site.objects.get_current())
        message = """<p>{}{}{}{}{}{}</p>""".format(section, name, email, phone, theme, comment)
        send_mail_contact(subject, message)


def send_mail_contact(subject, message):
    message = Mail(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_emails=[e.email for e in EmailsFeedback.objects.all()],
        subject=subject,
        html_content='{}'.format(message))
    try:
        sg = SendGridAPIClient(settings.EMAIL_HOST_PASSWORD)
        response = sg.send(message)
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)
    except Exception as e:
        print(e)

# def send_mail_contact(subject, message):
#     """Отправка email контакной формы"""
#     try:
#         send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [e.email for e in EmailsFeedback.objects.all()])
#         return True
#     except BadHeaderError:
#         return False
