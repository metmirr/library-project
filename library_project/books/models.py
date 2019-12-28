from django.db import models
from django.utils import timezone
import datetime


class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    isbn = models.CharField(max_length=13)
    publication_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
