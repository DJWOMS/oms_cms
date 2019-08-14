from django.core.management.base import BaseCommand

from oms_cms.backend.languages.models import Lang
from oms_cms.backend.news.models import Post, Category, Tags


class Command(BaseCommand):
    help = 'Add post'

    def handle(self, *args, **options):
        mini = """<p>OMS CMS написана на языке python3 и основана на framework django2. 
        Что позволяет вам без проблем расширить ее функционал.</p>"""
        text = """<p>OMS CMS написана на языке python3 и основана на framework django2. 
                Что позволяет вам без проблем расширить ее функционал.</p>
                <p>Данная cms позволяет сделать сайт за считанные минуту. Вы можете использовать базовый шаблон или 
                скачать с официального сайта.</p>"""
        category = Category.objects.create(name="Блог", slug="blog", lang=Lang.objects.get(is_default=True))
        tag = Tags.objects.create(name="oms", slug="oms")
        i = 10
        while i > 0:
            post = Post.objects.create(
                title="Новость-{}".format(i),
                mini_text=mini,
                text=text,
                slug="post-{}".format(i),
                category=category,
                lang=Lang.objects.get(is_default=True)
            )
            post.tag.add(tag)
            i -= 1
        self.stdout.write('Success add posts')
