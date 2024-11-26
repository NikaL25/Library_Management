import unittest
from library import Library
from models import Book


class TestLibrary(unittest.TestCase):

    def setUp(self):
        """Инициализация тестовой библиотеки перед каждым тестом."""
        self.library = Library()
        self.library.books = []  # Начинаем с пустой библиотеки

    def test_add_book(self):
        """Тест добавления книги."""
        self.library.add_book("Мастер и Маргарита", "Михаил Булгаков", 1967)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Мастер и Маргарита")

    def test_remove_book(self):
        """Тест удаления книги."""
        book = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)
        self.library.books.append(book)
        self.library.remove_book(book.id)
        self.assertEqual(len(self.library.books), 0)

    def test_search_books(self):
        """Тест поиска книги."""
        self.library.add_book("Мастер и Маргарита", "Михаил Булгаков", 1967)
        results = self.library.search_books("Мастер", "title")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Мастер и Маргарита")

    def test_update_status(self):
        """Тест изменения статуса книги."""
        book = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)
        self.library.books.append(book)
        self.library.update_status(book.id, "выдана")
        self.assertEqual(book.status, "выдана")

    def test_list_books(self):
        """Тест отображения всех книг."""
        self.library.add_book("Мастер и Маргарита", "Михаил Булгаков", 1967)
        self.library.add_book("1984", "Джордж Оруэлл", 1949)
        self.assertEqual(len(self.library.books), 2)


if __name__ == "__main__":
    unittest.main()
