from django.db import models

# Create your models here.

class BooksModel(models.Model):
    name_of_book = models.CharField(max_length=25, unique = True)
    name_of_author = models.CharField(max_length=25)
    pages = models.IntegerField()
