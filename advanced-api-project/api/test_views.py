from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.

    Covers:
    - CRUD operations
    - Filtering, searching, and ordering
    - Permission enforcement
    """

    def setUp(self):
        """
        Set up test data before each test.
        """

        # Create user for authentication tests
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        # Create author
        self.author = Author.objects.create(name="George Orwell")

        # Create books
        self.book1 = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )

        self.book2 = Book.objects.create(
            title="Animal Farm",
            publication_year=1945,
            author=self.author
        )

        # URLs
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')

    # ---------- READ TESTS ----------

    def test_list_books(self):
        """Anonymous user can list books"""

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_single_book(self):
        """Anonymous user can retrieve a single book"""

        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "1984")

    # ---------- CREATE TESTS ----------

    def test_create_book_unauthenticated(self):
        """Unauthenticated user cannot create a book"""

        data = {
            "title": "Homage to Catalonia",
            "publication_year": 1938,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        """Authenticated user can create a book"""

        self.client.login(username='testuser', password='testpass123')

        data = {
            "title": "Homage to Catalonia",
            "publication_year": 1938,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # ---------- UPDATE TESTS ----------

    def test_update_book_authenticated(self):
        """Authenticated user can update a book"""

        self.client.login(username='testuser', password='testpass123')

        url = reverse('book-update', args=[self.book1.id])
        data = {
            "title": "Nineteen Eighty-Four",
            "publication_year": 1949,
            "author": self.author.id
        }

        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Nineteen Eighty-Four")

    # ---------- DELETE TESTS ----------

    def test_delete_book_authenticated(self):
        """Authenticated user can delete a book"""

        self.client.login(username='testuser', password='testpass123')

        url = reverse('book-delete', args=[self.book2.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ---------- FILTER / SEARCH / ORDER TESTS ----------

    def test_filter_books_by_publication_year(self):
        """Filter books by publication year"""

        response = self.client.get(
            self.list_url + '?publication_year=1949'
        )

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "1984")

    def test_search_books_by_title(self):
        """Search books by title"""

        response = self.client.get(
            self.list_url + '?search=animal'
        )

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Animal Farm")

    def test_order_books_by_year_desc(self):
        """Order books by publication year descending"""

        response = self.client.get(
            self.list_url + '?ordering=-publication_year'
        )

        self.assertEqual(response.data[0]['title'], "1984")
