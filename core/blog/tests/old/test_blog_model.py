# from django.test import TestCase
#
# # from blog.forms import PostForm
# from blog.models import Post, Category
# from datetime import datetime
# from django.contrib.auth import get_user_model
# from accounts.models import User, Profile
#
#
# class TestPostModel(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(email="test@test.com", password="a/@12345678")
#         self.profile = Profile.objects.create(
#             user=self.user,
#             first_name="test_name",
#             last_name="test_last_name",
#             description="test_description",
#         )
#     def test_create_post_post_with_data(self):
#
#         post = Post.objects.create(
#             author=self.user,
#             title = "test",
#             content = "description",
#             status = True,
#             category = None,
#             published_date = datetime.now(),
#         )
#         self.assertTrue(Post.objects.filter(pk=post.id).exists())
#         self.assertEqual(post.title, "test")
