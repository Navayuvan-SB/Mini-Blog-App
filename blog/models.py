from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Author(models.Model):
    """Model representing an Author"""

    name = models.CharField(max_length=100, verbose_name='Author Name')
    bio = models.TextField('Description about the author')
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author-detail", kwargs={"pk": self.pk})


class Blog(models.Model):
    """Model representing a blog"""

    title = models.CharField(max_length=200, verbose_name='Blog Title')
    post_date = models.DateField('Posted Date')
    blogger = models.ForeignKey('Author', verbose_name='Author of the blog',
                                on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ['-post_date']


class Content(models.Model):
    """Model representing one Content of a blog"""

    text = models.TextField('Content text')
    blog = models.ForeignKey(
        'Blog', verbose_name="Content's blog", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Model representing one comment of a blog"""

    text = models.TextField('Comment text')
    blog = models.ForeignKey(
        'Blog', verbose_name="Comment's blog", on_delete=models.SET_NULL, null=True)

    comment_date = models.DateField('Commented Date')

    user = models.ForeignKey(
        User, verbose_name='Commented By', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-comment_date']
