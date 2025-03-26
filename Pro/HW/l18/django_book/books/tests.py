from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User


class BookAPITestCase(APITestCase):
    """
    Класс BookAPITestCase.
    """
    def setUp(self):
        """
        Создание тестовых пользователей и книг.
        :return:
        """
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.admin_user = User.objects.create_superuser(username="admin", password="admin123")

        for i in range(15):
            Book.objects.create(
                title=f"Book {i}", author="Test Author", genre="Fiction", publication_year=2021
            )

        self.book = Book.objects.create(
            title="Test Book", author="Test Author", genre="Fiction", publication_year=2021
        )

    def test_create_book(self):
        """
        Тестируем создание книги.
        :return:
        """
        self.client.login(username="testuser", password="password123")
        data = {'title': 'New Book', 'author': 'New Author', 'genre': 'Science Fiction', 'publication_year': 2022}
        response = self.client.post('/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthorized(self):
        """
        Тестируем создание книги без аутентификации (должно быть запрещено).
        :return:
        """
        data = {'title': 'New Book', 'author': 'New Author', 'genre': 'Science Fiction', 'publication_year': 2022}
        response = self.client.post('/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_books(self):
        """
        Тестируем получение списка книг.
        :return:
        """
        self.client.login(username="testuser", password="password123")
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data['results']), 0)

    def test_get_book_detail(self):
        """
        Тестируем получение подробной информации о книге.
        :return:
        """
        self.client.login(username="testuser", password="password123")
        response = self.client.get(f'/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        """
        Тестируем обновление книги.
        :return:
        """
        self.client.login(username="testuser", password="password123")
        data = {'title': 'Updated Book', 'author': 'Updated Author', 'genre': 'Non-Fiction', 'publication_year': 2023}
        response = self.client.put(f'/books/{self.book.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()  # Обновляем объект в базе данных
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book_admin(self):
        """
        Тестируем удаление книги администратором.
        :return:
        """
        self.client.login(username="admin", password="admin123")
        response = self.client.delete(f'/books/{self.book.id}/')
