from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User, Profile
from blog.models import Post, Category
from datetime import datetime


class TestBlogView(TestCase):
    def setUp(self):
        self.client = Client
        self.user = User.objects.create_user(
            email="test@test.com", password="a/@12345678"
        )
        self.profile = Profile.objects.create(
            user=self.user,
            first_name="test_name",
            last_name="test_last_name",
            description="test_description",
        )
        self.post = Post.objects.create(
            author=self.user,
            title="test",
            content="description",
            status=True,
            category=None,
            published_date=datetime.now(),
        )

    # def test_blog_index_url_successful_response(self):
    #     url = reverse('blog:blog_index')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue(str(response.content).find("index"))
    #     self.assertTemplateUsed(response, 'blog/index.html')
    # def test_blog_post_detail_Logged_in_response(self):
    #     self.client.force_login(self.user)
    #     url = reverse('blog:post-detail', kwargs={'pk': self.post.slug})
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_blog_post_detail_anonymouse_response(self):
    #     url = reverse('blog:post-detail', kwargs={'pk': self.post.id})
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 302)
