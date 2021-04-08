from django.test import TestCase


class CommonViewTest(TestCase):

    def test_root_redirect_to_blog(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/blog/', status_code=301)
