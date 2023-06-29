from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250, unique=True, default=None)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)


    def __str__(self):
        return self.title
