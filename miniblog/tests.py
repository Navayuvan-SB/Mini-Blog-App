from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Author

from django.urls import reverse

import datetime


class SignUpViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        test_user = User.objects.create_user(
            username='username', password='password')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/accounts/signup')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/sign_up_user.html')

    def test_view_forbidden_if_already_logged_in(self):
        login = self.client.login(username='username', password='password')
        response = self.client.get(reverse('signup'))
        self.assertRedirects(response, '/blog/')

    def test_view_creates_an_user(self):
        response = self.client.post(reverse('signup'), {
            'username': 'user1',
            'password1': 'testpress',
            'password2': 'testpress',
            'first_name': 'Henry',
            'last_name': 'James',
            'date_of_birth': '1998-06-11',
            'bio': 'A Sample Bio'
        })

        login = self.client.login(username='user1', password='testpress')
        self.assertTrue(login)

    def test_view_creates_an_author(self):
        response = self.client.post(reverse('signup'), {
            'username': 'user1',
            'password1': 'testpress',
            'password2': 'testpress',
            'first_name': 'Henry',
            'last_name': 'James',
            'date_of_birth': '1998-06-11',
            'bio': 'A Sample Bio'
        })

        user = User.objects.get(username='user1')
        author = Author.objects.get(name=user.get_full_name())

        self.assertEqual(author.date_of_birth, datetime.date(1998, 6, 11))

    def test_view_redirects_to_login_after_creation_of_user(self):
        response = self.client.post(reverse('signup'), {
            'username': 'user1',
            'password1': 'testpress',
            'password2': 'testpress',
            'first_name': 'Henry',
            'last_name': 'James',
            'date_of_birth': '1998-06-11',
            'bio': 'A Sample Bio'
        })

        self.assertRedirects(response, '/accounts/login/')
