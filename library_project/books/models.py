from django.db import models
from django.utils import timezone
import datetime


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    website = models.URLField(max_length=30)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    authors = models.ManyToManyField(Author, related_name="books")
    isbn = models.CharField(max_length=13)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

