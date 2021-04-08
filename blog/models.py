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
        return reverse("author_detail", kwargs={"pk": self.pk})
