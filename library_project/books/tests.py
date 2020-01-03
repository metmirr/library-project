import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Book


class BookMethodTests(TestCase):
    fixtures = ["data.json"]

    def test_recent_pub(self):
        futuredate = timezone.now().date() + datetime.timedelta(days=5)
        future_pub = Book(publication_date=futuredate)
