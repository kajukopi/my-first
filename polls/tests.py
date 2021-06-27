import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Blog


class BlogModelTests(TestCase):

    def test_was_published_recently_with_future_blog(self):

        time = timezone.now() + datetime.timedelta(days=30)
        future_blog = Blog(blog_date=time)
        self.assertIs(future_blog.was_published_recently(), False)

    def test_was_published_recently_with_old_blog(self):

        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_blog = Blog(blog_date=time)
        self.assertIs(old_blog.was_published_recently(), False)

    def test_was_published_recently_with_recent_blog(self):

        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_blog = Blog(blog_date=time)
        self.assertIs(recent_blog.was_published_recently(), True)

def create_blog(blog_text,blog_subject, days):

    time = timezone.now() + datetime.timedelta(days=days)
    return Blog.objects.create(blog_text=blog_text, blog_subject=blog_subject, blog_date=time)

class blogIndexViewTests(TestCase):
    def test_no_blogs(self):

        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_blog_list'], [])

    def test_past_blog(self):

        blog = create_blog(blog_text="Past blog.", blog_subject="Past blog subject 1.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_blog_list'],
            [blog],
        )

    def test_future_blog(self):

        create_blog(blog_text="Future blog.", blog_subject="Past blog subject 1.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_blog_list'], [])

    def test_future_blog_and_past_blog(self):

        blog = create_blog(blog_text="Past blog.", blog_subject="Past blog subject 1.", days=-30)
        create_blog(blog_text="Future blog.", blog_subject="Past blog subject 1.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_blog_list'],
            [blog],
        )

    def test_two_past_blogs(self):

        blog1 = create_blog(blog_text="Past blog 1.", blog_subject="Past blog subject 1.", days=-30)
        blog2 = create_blog(blog_text="Past blog 2.", blog_subject="Past blog subject 1.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_blog_list'],
            [blog2, blog1],
        )

class blogDetailViewTests(TestCase):
    def test_future_blog(self):

        future_blog = create_blog(blog_text='Future blog.', blog_subject="Past blog subject 1.", days=5)
        url = reverse('polls:detail', args=(future_blog.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_blog(self):

        past_blog = create_blog(blog_text='Past blog.', blog_subject="Past blog subject 1.", days=-5)
        url = reverse('polls:detail', args=(past_blog.id,))
        response = self.client.get(url)
        self.assertContains(response, past_blog.blog_text)
