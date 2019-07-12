from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Add users'

    def handle(self, *args, **options):
        # User.objects.create_user(
        #     username="test",
        #     password='Test123456',
        #     email="dghghj454556bnz@ya.r",
        #     is_superuser=True,
        #     is_staff=True)
        self.stdout.write('Success users')


