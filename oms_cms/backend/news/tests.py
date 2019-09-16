from datetime import timedelta

from django.conf import settings
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import Category, Post, Tags


class ViewsTestCase(TestCase):

    def setUp(self):
        self.now = timezone.now()
        self.yesterday = self.now - timedelta(days=1)
        self.tomorrow = self.now + timedelta(days=1)
        lang = settings.LANGUAGE_CODE

        tag = Tags.objects.create(name="TestTag", slug='tag_test')

        parent = Category.objects.create(name="TestCategory", lang=lang, slug='a')
        children = Category.objects.create(name="ChildrenCategory", parent=parent, lang=lang, slug='b')

        test_post = Post.objects.create(
            title="TestPost",
            category=parent,
            lang=lang,
            published_date=self.now,
            slug='c'
        )
        test_post.tag.add(tag)

        Post.objects.create(
            title="TestNews",
            category=children,
            lang=lang,
            published_date=self.now,
            slug='d'
        )

    def test_post_list(self):
        response = self.client.get(reverse('news:all-news'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], ['<Post: TestPost>', '<Post: TestNews>'])

    def test_category_post_list(self):
        response = self.client.get(reverse('news:list-news', kwargs={"slug": "a"}))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], ['<Post: TestPost>'])

    def test_post_detail(self):
        response = self.client.get(reverse('news:new-detail', kwargs={"category": "b", "post": "d"}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post'].title, 'TestNews')

    def test_tag_post_list(self):
        response = self.client.get(reverse('news:tag-news', kwargs={"tag": "tag_test"}))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], ['<Post: TestPost>'])
