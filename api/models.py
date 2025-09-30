from datetime import date
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=40)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )
    published_date = models.DateField(default=date.today)

    def __str__(self):
        return self.title
