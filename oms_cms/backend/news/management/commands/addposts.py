from django.core.management.base import BaseCommand

from oms_cms.backend.languages.models import Lang
from oms_cms.backend.news.models import Post, Category


class Command(BaseCommand):
    help = 'Add post'

    def handle(self, *args, **options):
        category = Category.objects.create(name="Блог", slug="blog", lang=Lang.objects.get(is_default=True))
        i = 10
        while i > 0:
            Post.objects.create(
                title="title-{}".format(i),
                mini_text="mini_text",
                text="text",
                slug="title-{}".format(i),
                category=category,
                lang=Lang.objects.get(is_default=True)
            )
            i -= 1
        self.stdout.write('Success add posts')
