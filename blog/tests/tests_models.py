from django.test import TestCase
from blog.models import Author


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Author.objects.create(
            name='Sam Willams', bio='A Sample bio with simple description', date_of_birth='2000-06-11')

    def test_name_label(self):
        author = Author.objects.get(id=1)
        name_label = author._meta.get_field('name').verbose_name

        self.assertEqual(name_label, 'Author Name')

    def test_bio_label(self):
        author = Author.objects.get(id=1)
        bio_label = author._meta.get_field('bio').verbose_name

        self.assertEqual(bio_label, 'Description about the author')

    def test_str_returns_author_name(self):
        author = Author.objects.get(id=1)
        self.assertEqual(str(author), 'Sam Willams')

    def test_get_absolute_url_returns_correct_url(self):
        author = Author.objects.get(id=1)

        self.assertEqual('blog/author/1', author.get_absolute_url())
