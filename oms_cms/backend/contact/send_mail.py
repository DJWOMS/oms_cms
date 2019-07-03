import os
from django.core.mail import send_mail, BadHeaderError
from oms_cms.config import settings
from oms_cms.backend.contact.models import EmailsFeedback

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


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
