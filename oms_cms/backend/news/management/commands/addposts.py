from django.core.management.base import BaseCommand
from oms_cms.backend.news.models import Post, Category


class Command(BaseCommand):
    help = 'Add post'

    def handle(self, *args, **options):
        category = Category.objects.create(name="Акция", slug="test")
        i = 10
        while i > 0:
            Post.objects.create(
                title="title-{}".format(i),
                mini_text="mini_text",
                text="text",
                slug="title-{}".format(i),
                category=category
            )
            i -= 1
        self.stdout.write('Success add posts')
