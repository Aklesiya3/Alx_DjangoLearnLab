from django.db import models
from django.utils import timezone

# Author model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book model
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # Optional: Custom method to validate publication_year
    def clean(self):
        from django.core.exceptions import ValidationError
        current_year = timezone.now().year
        if self.publication_year > current_year:
            raise ValidationError('Publication year cannot be in the future.')
