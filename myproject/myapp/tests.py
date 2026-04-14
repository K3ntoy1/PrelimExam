from django.test import TestCase
from .models import Book
from django.utils import timezone

# Create your tests here.

class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="1984",
            author="George Orwell",
            published_date=timezone.datetime(1949, 6, 8).date(),
        )

    def test_str_representation(self):
        self.assertEqual(str(self.book), "1984 by George Orwell")

    def test_book_fields(self):
        self.assertEqual(self.book.title, "1984")
        self.assertEqual(self.book.author, "George Orwell")
        self.assertEqual(self.book.published_date.year, 1949)

