from django.conf import settings
from django.core.management.base import BaseCommand

from oms_cms.backend.news.models import Post, Category, Tags


class Command(BaseCommand):
    help = 'Add post'

    def handle(self, *args, **options):
        mini = """<p>OMS CMS is written in python3 and is based on the django2 framework.
         That allows you to easily expand its functionality.</p>"""
        text = """<p>OMS CMS is written in python3 and is based on the django2 framework.
                 That allows you to easily expand its functionality.</p>
                 <p>This cms allows you to make a website in minutes. You can use the basic template 
                    or download from the official site.</p>"""
        category = Category.objects.create(name="Blog", slug="blog", lang=settings.LANGUAGE_CODE)
        tag = Tags.objects.create(name="oms", slug="oms")
        i = 10
        while i > 0:
            post = Post.objects.create(
                title="Article-{}".format(i),
                mini_text=mini,
                text=text,
                slug="post-{}".format(i),
                category=category,
                lang=settings.LANGUAGE_CODE
            )
            post.tag.add(tag)
            i -= 1
        self.stdout.write('Success add posts')
