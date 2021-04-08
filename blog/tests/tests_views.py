from django.test import TestCase


class IndexViewTest(TestCase):

    def test_root_redirect_to_blog(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/blog/', status_code=301)

    def test_context_has_correct_items(self):
        response = self.client.get('/blog/')

        self.assertTrue('total_number_of_blogs' in response.context)
        self.assertTrue('total_number_of_authors' in response.context)
