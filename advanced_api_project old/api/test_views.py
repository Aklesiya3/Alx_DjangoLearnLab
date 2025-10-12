#from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create an author
        self.author = Author.objects.create(name="J.K. Rowling")

        # Create a book
        self.book = Book.objects.create(
            title="Harry Potter",
            publication_year=1997,
            author=self.author
        )

        # Create a user
        self.user = User.objects.create_user(username="testuser", password="password123")

        # URLs
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])

    # -------------------------------
    # CRUD Tests
    # -------------------------------

    def test_get_books_list(self):
        """Test retrieving list of books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter")

    def test_get_single_book(self):
        """Test retrieving a single book by ID"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Harry Potter")

    def test_create_book_authenticated(self):
        """Test creating a book with authentication"""
        self.client.login(username="testuser", password="password123")
        data = {"title": "New Book", "publication_year": 2020, "author": self.author.id}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        """Test creating a book without login should fail"""
        data = {"title": "Unauthorized Book", "publication_year": 2020, "author": self.author.id}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        """Test updating an existing book"""
        self.client.login(username="testuser", password="password123")
        data = {"title": "Harry Potter Updated", "publication_year": 1998, "author": self.author.id}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Harry Potter Updated")

    def test_delete_book(self):
        """Test deleting a book"""
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # -------------------------------
    # Filtering, Searching, Ordering
    # -------------------------------

    def test_filter_books_by_title(self):
        response = self.client.get(f"{self.list_url}?title=Harry Potter")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Harry Potter")

    def test_search_books(self):
        response = self.client.get(f"{self.list_url}?search=rowling")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['author']['name'], "J.K. Rowling")

    def test_order_books_by_year(self):
        Book.objects.create(title="Newer Book", publication_year=2022, author=self.author)
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2022)
