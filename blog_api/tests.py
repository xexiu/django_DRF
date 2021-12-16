from blog.models import Category, Post
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class PostTests(APITestCase):

    def test_view_posts(self):
        """
        Ensure we can view all objects.
        """
        self.test_category = Category.objects.create(name='django')
        self.admin = User.objects.create_superuser(
            username='admin', password='12345')

        self.client.login(username=self.admin.username, password='12345')
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        self.test_category = Category.objects.create(name='django')
        self.testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')

        self.client.login(username=self.testuser1.username,
                          password='123456789')

        data = {
            'title': 'new',
            'author': 1,
            'excerpt': 'new',
            'content': 'new'
        }

        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_update(self):
        client = APIClient()
        self.test_category = Category.objects.create(name='django')
        self.testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')

        self.test_category = Category.objects.create(name='django')
        self.testuser2 = User.objects.create_user(
            username='test_user2', password='123456789')

        Post.objects.create(category_id=1, title='Post title', excerpt='Post Excerpt',
                                        content='Post Content', slug='post-title', author_id=1, status='published')

        client.login(username=self.testuser1.username,
                          password='123456789')

        url = reverse(('blog_api:detailcreate'), kwargs={'pk': 1})
        response = client.put(url, {
            'title': 'new',
            'author': 1,
            'excerpt': 'new',
            'content': 'new',
            'status': 'published'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
