import datetime
from django.utils import timezone
from django.test import TestCase
from .models import Book


class BookMethodTests(TestCase):
    def test_recent_pub(self):
        futuredate = timezone.now().date() + datetime.timedelta(days=5)
        future_pub = Book(publication_date=futuredate)
        self.assertEqual(future_pub.recent_publication(), False)
