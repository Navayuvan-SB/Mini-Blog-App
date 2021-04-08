from django.test import TestCase
from django.urls import reverse

from blog.models import Blog, Author, Content

import datetime


class IndexViewTest(TestCase):

    def test_root_redirect_to_blog(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/blog/', status_code=301)

    def test_context_has_correct_items(self):
        response = self.client.get('/blog/')

        self.assertTrue('total_number_of_blogs' in response.context)
        self.assertTrue('total_number_of_authors' in response.context)


class BlogListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        test_author = Author.objects.create(
            name="James", date_of_birth='1998-06-11')

        number_of_contents = 3
        for content_id in range(number_of_contents):
            Content.objects.create(text=f'Sample Text {content_id}')

        all_test_contents = Content.objects.all()

        current_date = datetime.date.today()
        date_of_day_before = datetime.date.today() - datetime.timedelta(days=1)

        number_of_blog = 17
        for blog_id in range(number_of_blog):
            test_blog = Blog.objects.create(
                title=f'Title {blog_id}',
                post_date=current_date if blog_id % 2 == 0 else date_of_day_before,
                blogger=test_author
            )

            test_blog.content_set.set(all_test_contents)
            test_blog.save()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/blogs/')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['blog_list']) == 5)

    def test_lists_all_authors(self):
        response = self.client.get(reverse('blogs') + '?page=4')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['blog_list']) == 2)
