from django.test import TestCase


class APITestCase(TestCase):
    def test_book_count(self):
        response = self.client.get("/api/")
        self.assertEqual(response.status_code, 200)
