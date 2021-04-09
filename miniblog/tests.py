from django.test import TestCase
from django.contrib.auth.models import User

from django.urls import reverse


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
            'password2': 'testpress'
        })

        login = self.client.login(username='user1', password='testpress')
        self.assertTrue(login)

    def test_view_redirects_to_login_after_creation_of_user(self):
        response = self.client.post(reverse('signup'), {
            'username': 'user1',
            'password1': 'testpress',
            'password2': 'testpress'
        })

        self.assertRedirects(response, '/accounts/login/')
