from django.test import TestCase
from blog.models import Author


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Author.objects.create(
            name='Sam Willams', bio='A Sample bio with simple description', date_of_birth='11/06/2000')
