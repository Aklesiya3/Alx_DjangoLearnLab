from django.db import models

# Create your models here.

class Author (models.Model):
    # This model stores information about an Author
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name
class Book (models.Model):
     # This model stores information about a Book
    title=models.CharField(max_length=200)
    publication_year=models.ImtegerField()
    # ForeignKey creates the link between Book and Author
    author= models.Foreignkey(Author, related_name='books', on_delete=models.CASCADE)

    def _str_(self):
        return self.title
