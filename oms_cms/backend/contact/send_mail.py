from django.conf import settings
from oms_cms.backend.utils.models import EmailsFeedback

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_mail_contact(subject, message):
    """Отправка письма через SendGrid"""
    message = Mail(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_emails=[e.email for e in EmailsFeedback.objects.all()],
        subject=subject,
        html_content='{}'.format(message))
    try:
        sg = SendGridAPIClient(settings.EMAIL_HOST_PASSWORD)
        response = sg.send(message)
        print("good")
        print(response)
    except Exception as e:
        print("bad")
        print(e)
