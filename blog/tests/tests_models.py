from django.test import TestCase
from blog.models import Author, Content, Comment

import datetime


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

        self.assertEqual('/blog/author/1', author.get_absolute_url())


class ContentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Content.objects.create(
            text='A Sample Test with simple description'
        )

    def test_text_label(self):
        content = Content.objects.get(id=1)
        text_label = content._meta.get_field('text').verbose_name

        self.assertEqual(text_label, 'Content text')

    def test_str_returns_content_text(self):
        content = Content.objects.get(id=1)
        self.assertEqual(str(content), 'A Sample Test with simple description')


class CommentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        current_date = datetime.date.today()

        Comment.objects.create(
            text='A Sample Comment with simple description',
            comment_date=current_date
        )

    def test_text_label(self):
        comment = Comment.objects.get(id=1)
        text_label = comment._meta.get_field('text').verbose_name

        self.assertEqual(text_label, 'Comment text')

    def test_comment_date_label(self):
        comment = Comment.objects.get(id=1)
        comment_date_label = comment._meta.get_field(
            'comment_date').verbose_name

        self.assertEqual(comment_date_label, 'Commented Date')

    def test_str_returns_comment_text(self):
        comment = Comment.objects.get(id=1)
        self.assertEqual(
            str(comment), 'A Sample Comment with simple description')
