from django.db import models
from django.urls import reverse


class Author(models.Model):
    """Model representing an Author"""

    name = models.CharField(max_length=100, verbose_name='Author Name')
    bio = models.TextField('Description about the author')
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author-detail", kwargs={"pk": self.pk})


class Content(models.Model):
    """Model representing one Content of a blog"""

    text = models.TextField('Content text')

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Model representing one comment of a blog"""

    text = models.TextField('Comment text')
    comment_date = models.DateField('Commented Date')

    def __str__(self):
        return self.text
